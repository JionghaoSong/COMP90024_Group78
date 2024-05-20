from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import csv
import os
from dotenv import load_dotenv
import uuid

# load env
load_dotenv()

client = Elasticsearch(
    "https://localhost:9200",
    basic_auth=("elastic", os.getenv("ELASTIC_PSW")),
    verify_certs=False,
    timeout=60
)

print(client.info())


def insert_liquor_data(file_name, batch_size=1000):
    with open(file_name, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        reader.fieldnames = [field.strip() for field in reader.fieldnames]
        print("CSV Columns:", reader.fieldnames)
        actions = []
        for row in reader:
            action = {
                "_index": "liquor",
                "_id": str(uuid.uuid4()),
                "_source": {
                    "objectid": int(row["objectid"]),
                    "premises_name": row["premises_name"],
                    "long": float(row["long"]),
                    "lat": float(row["lat"]),
                    "lga": row["lga"]
                }
            }
            actions.append(action)

            if len(actions) >= batch_size:
                response = bulk(client, actions)
                print(f"Inserted {len(actions)} documents")
                actions = []

        if actions:
            response = bulk(client, actions)
            print(f"Inserted {len(actions)} documents")


insert_liquor_data('vic_liquor_venues.csv')
