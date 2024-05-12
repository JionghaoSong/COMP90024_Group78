import json
import sys
import threading
from constant.servers import *
from helper.statuses import get_timelines, get_unique_tags
from helper.utils import write_result, get_unique_tags

# validate arguments
if len(sys.argv) < 2:
    print("Usage: python3 harvester.py OUTPUT_DIR")
    exit(0)

OUTPUT_DIR = sys.argv[1]
N_YEAR = 1
count_dict = {}

# clear output file
# with open(f"{OUTPUT_DIR}/rows.json", 'w') as f:
#     f.write('')

def fetch_timelines(server, output_file):
    token = ACCESS_TOKENS[server] if server in ACCESS_TOKENS else ""
    count = get_timelines(token, f"https://{server}", N_YEAR, output_file=output_file, local=True)
    # with open(output_file, 'a') as f:
    #     json.dump({server: count}, f)

# fetch and get statuses from each server
for server in POPULAR_SERVERS:
    print(f"Start fetching: {server}")
    output_file = f"{OUTPUT_DIR}/{server.replace('.', '_')}.json"
    threading.Thread(target=fetch_timelines, args=(server, output_file)).start()

