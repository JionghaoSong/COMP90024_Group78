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


def create_pedestrian_index():
    pc = "pedestrian_counting"
    index_body = {
        "settings": {
            "index": {
                "number_of_shards": 3,
                "number_of_replicas": 1
            }
        },
        "mappings": {
            "properties": {
                "Sensor_Name": {"type": "text"},
                "SensingDateTime(Hour)": {"type": "date"},
                "LocationID": {"type": "integer"},
                "Direction_1": {"type": "integer"},
                "Direction_2": {"type": "integer"},
                "Total_of_Directions": {"type": "integer"},
                "Location": {"type": "geo_point"}
            }
        }
    }
    if client.indices.exists(index=pc):
            client.indices.delete(index=pc)
            print(f"Deleted existing index '{pc}'.")

    response = client.indices.create(index=pc, body=index_body)
    if 'acknowledged' in response and response['acknowledged']:
        print("Index creation acknowledged.")
    else:
        print("Index creation failed:", response)
    return response



create_pedestrian_index()
