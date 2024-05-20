from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk, BulkIndexError
import csv
import os
from dotenv import load_dotenv
import uuid

# Load environment variables
load_dotenv()

# Initialize Elasticsearch client
client = Elasticsearch(
    "https://localhost:9200",
    basic_auth=("elastic", os.getenv("ELASTIC_PSW")),
    verify_certs=False,
    timeout=60
)

# Print client info to verify connection
print(client.info())

def insert_accident_data(file_name, batch_size=500):
    try:
        with open(file_name, 'r', encoding='utf-8-sig') as file:  # Use 'utf-8-sig' to handle BOM
            reader = csv.DictReader(file)
            reader.fieldnames = [field.strip() for field in reader.fieldnames]  # Clean up field names
            print("CSV Columns:", reader.fieldnames)
            actions = []

            for row in reader:
                action = {
                    "_index": "accidents",  # Specify the "accidents" index
                    "_id": str(uuid.uuid4()),  # Generate a unique ID for each document
                    "_source": {
                        "objectid": int(row["OBJECTID"]),
                        "accident_date": row["ACCIDENT_DATE"],
                        "day_of_week": row["DAY_OF_WEEK"],
                        "longitude": float(row["LONGITUDE"]),
                        "latitude": float(row["LATITUDE"]),
                        "alcoholtime": row["ALCOHOLTIME"],
                        "accident_type": row["ACCIDENT_TYPE"],
                        "light_condition": row["LIGHT_CONDITION"],
                        "speed_zone": row["SPEED_ZONE"],
                        "lga_name": row["LGA_NAME"]
                    }
                }
                actions.append(action)

                # Bulk insert when the batch size is reached
                if len(actions) >= batch_size:
                    bulk(client, actions)
                    print(f"Inserted {len(actions)} documents")
                    actions = []  # Reset the action list

            # Insert any remaining actions
            if actions:
                bulk(client, actions)
                print(f"Inserted {len(actions)} documents")

    except BulkIndexError as e:
        print("Bulk indexing operation encountered errors:")
        for i, error in enumerate(e.errors):
            print(f"Error {i+1}: {error}")

# Specify the path to your CSV file
insert_accident_data('data/Road_Crashes_Victoria.csv')
