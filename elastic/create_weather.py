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


def create_weather_index():
    index_name = "weather_station"
    index_body = {
        "settings": {
            "index": {
                "number_of_shards": 3,
                "number_of_replicas": 1
            }
        },
        "mappings": {
            "properties": {
                "dev_id": {"type": "keyword"},
                "date_measure": {"type": "date"},
                "RTC": {"type": "long"},
                "battery": {"type": "float"},
                "solarPanel": {"type": "float"},
                "command": {"type": "integer"},
                "solar": {"type": "float"},
                "precipitation": {"type": "float"},
                "strikes": {"type": "integer"},
                "windSpeed": {"type": "float"},
                "windDirection": {"type": "float"},
                "gustSpeed": {"type": "float"},
                "vapourPressure": {"type": "float"},
                "atmosphericPressure": {"type": "float"},
                "relativeHumidity": {"type": "integer"},
                "airTemp": {"type": "float"},
                "Location": {"type": "geo_point"},
                "Sensor_Name": {"type": "text"}
            }
        }
    }
    if client.indices.exists(index=index_name):
            client.indices.delete(index=index_name)
            print(f"Deleted existing index '{index_name}'.")

    response = client.indices.create(index=index_name, body=index_body)
    if 'acknowledged' in response and response['acknowledged']:
        print("Index creation acknowledged.")
    else:
        print("Index creation failed:", response)
    return response


create_weather_index()
