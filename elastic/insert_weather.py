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

def insert_weather_station_data(file_name, batch_size=1000):
    with open(file_name, 'r', encoding='utf-8-sig') as file:  
        reader = csv.DictReader(file)
        reader.fieldnames = [field.strip() for field in reader.fieldnames] 
        print("CSV Columns:", reader.fieldnames)  
        actions = []
        for row in reader:
            if row["Lat Long"]:  
                lat, lon = map(float, row["Lat Long"].split(','))
            else:
                lat, lon = None, None
            action = {
                "_index": "weather_station",
                "_id": f'{row["dev_id"]}_{row["date_measure"]}', 
                "_source": {
                    "dev_id": row["dev_id"],
                    "date_measure": row["date_measure"],
                    "RTC": int(row["RTC"]) if row["RTC"] else None,
                    "battery": float(row["battery"]) if row["battery"] else None,
                    "solarPanel": float(row["solarPanel"]) if row["solarPanel"] else None,
                    "command": int(row["command"]) if row["command"] else None,
                    "solar": float(row["solar"]) if row["solar"] else None,
                    "precipitation": float(row["precipitation"]) if row["precipitation"] else None,
                    "strikes": int(row["strikes"]) if row["strikes"] else None,
                    "windSpeed": float(row["windSpeed"]) if row["windSpeed"] else None,
                    "windDirection": float(row["windDirection"]) if row["windDirection"] else None,
                    "gustSpeed": float(row["gustSpeed"]) if row["gustSpeed"] else None,
                    "vapourPressure": float(row["vapourPressure"]) if row["vapourPressure"] else None,
                    "atmosphericPressure": float(row["atmosphericPressure"]) if row["atmosphericPressure"] else None,
                    "relativeHumidity": int(row["relativeHumidity"]) if row["relativeHumidity"] else None,
                    "airTemp": float(row["airTemp"]) if row["airTemp"] else None,
                    "Location": {"lat": lat, "lon": lon} if lat and lon else None,
                    "Sensor_Name": row["Sensor Name"]
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


insert_weather_station_data('weather_dataset.csv')
