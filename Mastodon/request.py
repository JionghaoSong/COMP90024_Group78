import time
from time import sleep
import aiohttp
import asyncio
import requests
import json
import re
from datetime import datetime, timedelta
from textblob import TextBlob
import string
from cleaner import remove_html_tags


# Key list: A list of keyword to search
def search_params(key_list: list):
    p = '&'.join(map(lambda x: f"any[]={x}", key_list))
    return p


# def get_url():
#     return "https://mastodon.social/tags/australia"
#     # return "https://aus.social/explore"


async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()


async def get_urls_concurrently():
    urls = [
        "https://mastodon.social/tags/australia",
        "https://aus.social/explore"
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
    return results


def get_tokens(content):
    def split_with_punc(s):
        r = re.split(r'[^\w\s]]+', s)
        return [a for a in r if a != '']

    # remove all emojis and UTF-8 characters
    def remove_unicode(s):
        a_en = s.encode("ascii", "ignore")
        return a_en.decode().strip().lower()

    def split_with_space(s):
        return [a for a in s.split(' ') if a != '']

    def remove_invalid(s):
        return re.sub(r'(?:@|http|https|#|[0-9])\S*', '', s).strip()

    def remove_punc(s):
        return ''.join(c for c in s if c not in string.punctuation)

    def concat_all(s_list):
        return [j for i in s_list for j in i]

    def remove_short(s_list):
        return [a for a in s_list if len(a) > 2]

    content = remove_unicode(content)
    content = remove_invalid(content)
    tokens = split_with_space(content)
    tokens = concat_all(list(map(split_with_punc, tokens)))
    return list(set(remove_short(tokens)))


# extract information from status
def extract_info(status):
    s = {}
    s['id'] = str(status['id'])
    s['created_at'] = status['created_at']
    s['lang'] = status['language']
    s['sentiment'] = TextBlob(status['content']).sentiment.polarity
    s['tokens'] = get_tokens(remove_html_tags(status['content']))
    # s['content'] = remove_html_tags(status['content'])
    s['tags'] = [t['name'] for t in status['tags']]

    if not s['tags'] and not s['tokens']:
        return None
    return s


def create_search_url(scope: str, key_list: list, max_id: str = None, local: bool = False):
    instance_url = get_url()  # Using the get_url function to obtain the base URL
    params = scope + '?' + \
             search_params(key_list) + \
             (f'&max_id={max_id}' if max_id else '') + \
             '&limit=40' + \
             ('&local=true' if local else '')
    return f"{instance_url}/api/v1/timelines/tag/{params}"


def get_timelines_tags(access_token, scope, nyears, key_list, local: bool = False, aus_only: bool = False):
    statuses = []
    instance_url = get_urls_concurrently
    headers = {'Authorization': f'Bearer {access_token}'}
    date_limit = datetime.now() - timedelta(days=365 * nyears)
    max_id = None

    while True:
        search_url = create_search_url(scope, key_list, instance_url, max_id, local=local)
        response = requests.get(search_url, headers=headers)
        data = json.loads(response.text)
        if data:
            print(f"get statuses from {data[0]['created_at']}")
            for status in data:
                created_at = datetime.strptime(status['created_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
                if created_at > date_limit and status['language'] == 'en':
                    statuses.append(extract_info(status))
                else:
                    break
            max_id = data[-1]['id']
        else:
            break
    return statuses


# def create_timelines_url(instance_url: str, max_id: str = None, local: bool = False):
#     params = f'limit=40' + \
#              (f'max_id={max_id}' if max_id else '') + \
#              ('&local=true' if local else '')
#     return f"{instance_url}/api/v1/timelines/public?{params}"

def create_timelines_url(instance_url: str, max_id: str = None, local: bool = False):
    params = ['limit=40']
    if max_id:
        params.append(f'max_id={max_id}')
    if local:
        params.append('local=true')
    params_string = '&'.join(params)
    return f"{instance_url}/api/v1/timelines/public?{params_string}"


def get_timelines(access_token, instance_url, nyears, headers, output_file: str, local: bool = False):
    headers['Authorization'] = f"Bearer {access_token}"
    with open(output_file, 'w') as f:
        f.write('')
    date_limit = datetime.now() - timedelta(days=365 * nyears)
    max_id = None
    count = 0

    while True:
        try:
            search_url = create_timelines_url(instance_url, max_id, local=local)
            response = requests.get(search_url, headers=headers)
            sleep(1)  # Throttling to avoid hitting rate limits
        except Exception as e:
            print("[Error] Requesting timelines:", str(e))
            continue

        try:
            data = json.loads(response.text)
        except json.decoder.JSONDecodeError:
            print("[Warning] Failed to decode JSON:", response.text)
            continue  # Skip this iteration and proceed with the next

        if data:
            if 'error' in data:
                print("[Error] Requesting timelines:", data['error'])
                if data["error"] == "Too many requests":
                    sleep(10)
                continue

            try:
                print(f"get statuses from {data[0]['created_at']}")
                for status in data:
                    created_at = datetime.strptime(status['created_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
                    if created_at >= date_limit and status['language'] == 'en':
                        s = extract_info(status)
                        if s:
                            count += 1
                            with open(output_file, 'a') as f:
                                json.dump(s, f)
                                f.write('\n')
                    else:
                        continue  # Skip processing this status and continue with the next one
                if data[-1]['id'] != max_id:
                    max_id = data[-1]['id']
                else:
                    print(f"max_id not updated: {max_id}")
                    break

            except Exception as e:
                print("[Error] Getting status data:", str(e))
                continue
        else:
            print("No data returned")
            break
    return count

