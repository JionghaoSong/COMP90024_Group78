from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import json
import os
from dotenv import load_dotenv

# load env 
load_dotenv()

client = Elasticsearch(
  "https://localhost:9200",
  basic_auth = ("elastic", os.getenv("ELASTIC_PSW")),
  verify_certs = False,
  timeout=60  
)

print(client.info())

def insert_mastodon_data(file_name, batch_size=1000):
    with open(file_name, 'r', encoding='utf-8') as file:
        actions = []
        for line in file:
            doc = json.loads(line)
            action = {
                "_index": "mastodon_social",
                "_id": doc["id"],
                "_source": doc
            }
            actions.append(action)
            
            if len(actions) >= batch_size:
                response = bulk(client, actions)
                print(f"Inserted {len(actions)} documents")
                actions = [] 
        
        if actions:
            response = bulk(client, actions)
            print(f"Inserted {len(actions)} documents")

insert_mastodon_data('../Mastodon/aus_social.json')
insert_mastodon_data('../Mastodon/amastodon_social.json')