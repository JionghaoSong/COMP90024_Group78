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
  basic_auth = ("elastic", os.getenv("ELASTIC_PSW")),
  verify_certs = False,
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
                    "premises_name": row["premises_name"],
                    "suburb": row["suburb"],
                    "licence_no": row["licence_no"],
                    "address_1": row["address_1"],
                    "address_2": row["address_2"],
                    "postcode": int(row["postcode"]),
                    "long": float(row["long"]),
                    "licence_category": row["licence_category"],
                    "objectid": int(row["objectid"]),
                    "lga": row["lga"],
                    "lat": float(row["lat"])
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


insert_liquor_data('mel_liquor_venues.csv')
