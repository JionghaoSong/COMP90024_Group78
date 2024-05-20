from elasticsearch import Elasticsearch
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Elasticsearch client
client = Elasticsearch(
    "https://localhost:9200",
    basic_auth=("elastic", os.getenv("ELASTIC_PSW")),
    verify_certs=False
)

# Print client info to verify connection
print(client.info())


def create_accident_index():
    accident = "accidents"
    index_body = {
        "settings": {
            "index": {
                "number_of_shards": 3,
                "number_of_replicas": 1
            }
        },
        "mappings": {
            "properties": {
                "objectid": {"type": "integer"},
                "accident_date": {"type": "date"},
                "day_of_week": {"type": "keyword"},
                "longitude": {"type": "float"},
                "latitude": {"type": "float"},
                "alcoholtime": {"type": "keyword"},
                "accident_type": {"type": "text"},
                "light_condition": {"type": "text"},
                "speed_zone": {"type": "text"},
                "lga_name": {"type": "keyword"}
            }
        }
    }

    if client.indices.exists(index=accident):
        client.indices.delete(index=accident)
        print(f"Deleted existing index '{accident}'.")

    response = client.indices.create(index=accident, body=index_body)
    if 'acknowledged' in response and response['acknowledged']:
        print("Index creation acknowledged.")
    else:
        print("Index creation failed:", response)

    return response


# Call the function to create the index
create_accident_index()
