from time import sleep
import requests
import json
import re
from datetime import datetime, timedelta
from textblob import TextBlob
import string

from utils import contains_any
from htmlParser import remove_html_tags

# Key list: A list of keyword to search
def search_params(key_list: list):
    p = '&'.join(map(lambda x: f"any[]={x}", key_list))
    return p

def get_tokens(content):
    def split_with_puncs(s):
        return [re.split(r'\W+', s) for a in s if a != '']

    def split_with_space(s):
        return [a for a in s.split(' ') if a != '']

    def remove_invalid(s):
        return re.sub(r'(?::|;|=)(?:-)?(?:\)|\(|D|P)', '', s).strip()

    def remove_puncs(s):
        return ''.join(c for c in s if c not in string.punctuation)

    def concat_all(s_list):
        return [j for i in s_list for j in i]

    def remove_shorts(s_list):
        return [a for a in s_list if len(a) > 2]

    # remove all emojis and UTF-8 characters
    def remove_unicode(s):
        return s.encode('ascii', 'ignore').decode().strip().lower()

    content = remove_unicode(content)
    content = remove_invalid(content)
    tokens = split_with_space(content)
    tokens = concat_all(list(map(split_with_puncs, tokens)))
    return list(set(remove_short(tokens)))

# extract information from status
def extract_info(status):
    s = {}
    s['id'] = str(status['id'])
    s['created_at'] = status['created_at']
    s['lang'] = status['language']
    s['sentiment'] = TextBlob(status['content']).sentiment.polarity
    tokens = get_tokens(remove_html_tags(status['content']))
    s['tokens'] = tokens
    s['tags'] = remove_html_tags(status['content'])
    if not s['tags'] and not s['tokens']:
        return None
    return s

def create_search_url(scope: str, key_list: list, instance_url: str, max_id=None, local: bool = False, aus_only: bool = False):
    search_params = '+'.join(map(lambda x: f"any[]={x}", key_list))
    params = f"&max_id={max_id}" if max_id else ""
    params += "&local=true" if local else ""
    return f"{instance_url}/api/v1/timelines/tag/{scope}?{search_params}{params}"

def get_timelines_tags(access_token, scope, nyears, key_list, local: bool = False, aus_only: bool = False):
    statuses = []
    instance_url = get_url(aus_only)
    headers = {'Authorization': f'Bearer {access_token}'}
    date_limit = datetime.datetime.now() - datetime.timedelta(days=365*nyears)
    statuses_scope = []
    max_id = None

    while True:
        search_url = create_search_url(scope, key_list, instance_url, max_id, local=local)
        response = requests.get(search_url, headers=headers)
        data = json.loads(response.text)
        if data:
            print(f"get statuses from {data[0]['created_at']}")
            for status in data:
                created_at = datetime.datetime.strptime(status['created_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
                if created_at > date_limit:
                    statuses_scope.append(extract_info(status))
                else:
                    break
            max_id = data[-1]['id']
        else:
            break
    return statuses_scope

def create_timelines_url(instance_url: str, max_id: str = None, local: bool = False):
    params = f"&max_id={max_id}" if max_id else ""
    params += "&local=true" if local else ""
    return f"{instance_url}/api/v1/timelines/public?{params}"

def get_url(aus_only: bool):
    # This function should return the URL based on whether aus_only is True or False
    # Since we don't know the real URLs, I'll just return a placeholder URL
    return "https://your.instance.url"

def extract_info(status):
    # Placeholder function to simulate extraction of info from status
    # Implement this according to your specific needs
    return {
        "id": status.get('id'),
        "content": status.get('content')
    }

def get_timelines(access_token, instance_url, nyears, output_file, local=False):
    headers = {'Authorization': f'Bearer {access_token}'}
    with open(output_file, 'w') as f:
        f.write('')
    date_limit = datetime.datetime.now() - datetime.timedelta(days=365 * nyears)
    max_id = None
    count = 0

    while True:
        try:
            search_url = create_search_url(instance_url, max_id, local)
            response = requests.get(search_url, headers=headers)
        except Exception as e:
            print(f"[Error] Requesting timelines:", str(e))
            continue

        time.sleep(1)  # sleep to prevent hitting API rate limits

        try:
            data = json.loads(response.text)
            if 'error' in data:
                print("[Error] Requesting timelines:", data["error"])
                if data["error"] == "Too many requests":
                    time.sleep(10)
                continue
        except Exception as e:
            print("[Error] Loading JSON:", str(e))
            continue

        if not data:
            print("No data returned")
            break

        try:
            print(f"get statuses from {data[0]['created_at']}")
            for status in data:
                created_at = datetime.datetime.strptime(status['created_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
                if created_at > date_limit:
                    s = extract_info(status)
                    if s:
                        count += 1
                        with open(output_file, 'a') as f:
                            json.dump(s, f)
                            f.write('\n')
                else:
                    print(f"id: {status['id']} reached date limit")
                    return count
            max_id = data[-1]['id']
            if max_id == data[0]['id']:  # Check if max_id was not updated
                print("max_id not updated (max_id)")
                break
        except Exception as e:
            print("[Error] Getting status data:", str(e))
            print("data:", json.dumps(data))
            continue

    return count


def create_search_url(instance_url, max_id, local):
    params = f"&max_id={max_id}" if max_id else ""
    params += "&local=true" if local else ""
    return f"{instance_url}/api/v1/timelines/public?{params}"


def extract_info(status):
    # Placeholder function to simulate extraction of info from status
    # Implement this according to your specific needs
    return {
        "id": status.get('id'),
        "content": status.get('content')
    }
