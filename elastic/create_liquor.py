from elasticsearch import Elasticsearch
import os
from dotenv import load_dotenv

# load env 
load_dotenv()


client = Elasticsearch(
  "https://localhost:9200",
  basic_auth = ("elastic", os.getenv("ELASTIC_PSW")),
  verify_certs = False
)

print(client.info())


def create_liquor_index():
    liquor = "liquor"
    index_body = {
        "settings": {
            "index": {
                "number_of_shards": 3,
                "number_of_replicas": 1
            }
        },
        "mappings": {
            "properties": {
                "premises_name": {"type": "text"},
                "suburb": {"type": "keyword"},
                "licence_no": {"type": "keyword"},
                "address_1": {"type": "text"},
                "address_2": {"type": "text"},
                "postcode": {"type": "integer"},
                "long": {"type": "float"},
                "licence_category": {"type": "text"},
                "objectid": {"type": "integer"},
                "lga": {"type": "keyword"},
                "lat": {"type": "float"}
            }
        }
    }
    if client.indices.exists(index=liquor):
            client.indices.delete(index=liquor)
            print(f"Deleted existing index '{liquor}'.")

    response = client.indices.create(index=liquor, body=index_body)
    if 'acknowledged' in response and response['acknowledged']:
        print("Index creation acknowledged.")
    else:
        print("Index creation failed:", response)
    return response



create_liquor_index()
