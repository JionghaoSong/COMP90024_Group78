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

def insert_ped_data(file_name, batch_size=1000):
    with open(file_name, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        reader.fieldnames = [field.strip() for field in reader.fieldnames]  
        print("CSV Columns:", reader.fieldnames)  
        actions = []
        for row in reader:
            lat, lon = map(float, row["Location"].split(','))
            action = {
                "_index": "pes_counting",
                "_id": f'{row["LocationID"]}_{row["SensingDateTime(Hour)"]}', 
                "_source": {
                    "Sensor_Name": row["Sensor_Name"],
                    "SensingDateTime(Hour)": row["SensingDateTime(Hour)"],
                    "LocationID": int(row["LocationID"]),
                    "Direction_1": int(row["Direction_1"]),
                    "Direction_2": int(row["Direction_2"]),
                    "Total_of_Directions": int(row["Total_of_Directions"]),
                    "Location": {
                        "lat": lat,
                        "lon": lon
                    }
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


insert_ped_data('/data/pedestrian-counting-system-monthly-counts-per-hour.csv')
