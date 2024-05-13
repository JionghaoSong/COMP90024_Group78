# import json
# import sys
# import threading
# from server import *
# from request import get_timelines
#
# # from utils import write_result, get_unique_tags
#
# # validate arguments
# if len(sys.argv) < 2:
#     print("Usage: python3 harvester.py OUTPUT_DIR")
#     exit(0)
#
# OUTPUT_DIR = sys.argv[1]
# N_YEAR = 1
# count_dict = {}
#
#
# # clear output file
# # with open(f"{OUTPUT_DIR}/rows.json", 'w') as f:
# #     f.write('')
#
# def fetch_timelines(server, output_file):
#     token = ACCESS_TOKENS[server] if server in ACCESS_TOKENS else ""
#     count = get_timelines(token, f"https://{server}", N_YEAR, output_file=output_file, local=True)
#
#
# # fetch and get statuses from each server
# for server in POPULAR_SERVERS:
#     print("Start fetching:", server)
#     output_file = f"{OUTPUT_DIR}/{server.replace('.', '_')}.json"
#     threading.Thread(target=fetch_timelines, args=(server, output_file)).start()

import sys
import threading
import random
from server import *
from request import get_timelines

# 10个不同的User-Agents
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 10; SM-A505FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15",
    "Opera/9.80 (Windows NT 6.1; WOW64) Presto/2.12.388 Version/12.18",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko"
]

# validate arguments
if len(sys.argv) < 2:
    print("Usage: python3 harvester.py OUTPUT_DIR")
    exit(0)

OUTPUT_DIR = sys.argv[1]
N_YEAR = 1
count_dict = {}


def fetch_timelines(server, output_file):
    token = ACCESS_TOKENS[server] if server in ACCESS_TOKENS else ""
    headers = {'User-Agent': random.choice(USER_AGENTS)}  # 随机选择一个User-Agent
    # 确保传递 headers 参数
    count = get_timelines(token, f"https://{server}", N_YEAR, headers=headers, output_file=output_file, local=True)


# fetch and get statuses from each server
for server in POPULAR_SERVERS:
    print("Start fetching:", server)
    output_file = f"{OUTPUT_DIR}/{server.replace('.', '_')}.json"
    threading.Thread(target=fetch_timelines, args=(server, output_file)).start()
