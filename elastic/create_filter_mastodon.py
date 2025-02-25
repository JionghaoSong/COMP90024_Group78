from elasticsearch import Elasticsearch
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

def create_melbourne_mastodon_social_index():
    melbourne_mastodon_social = "melbourne_mastodon_social"
    index_body = {
        "settings": {
            "index": {
                "number_of_shards": 3,
                "number_of_replicas": 1
            }
        },
         "mappings": {
            "properties": {
                "id": {"type": "keyword"}, 
                "created_at": {"type": "date"}, 
                "lang": {"type": "keyword"}, 
                "sentiment": {"type": "float"}, 
                "tokens": {"type": "text"},
                "tags": {"type": "keyword"} 
            }
        }
    }
    if client.indices.exists(index=melbourne_mastodon_social):
            client.indices.delete(index=melbourne_mastodon_social)
            print(f"Deleted existing index '{melbourne_mastodon_social}'.")

    response = client.indices.create(index=melbourne_mastodon_social, body=index_body)
    if 'acknowledged' in response and response['acknowledged']:
        print("Index creation acknowledged.")
    else:
        print("Index creation failed:", response)
    return response



create_melbourne_mastodon_social_index()
