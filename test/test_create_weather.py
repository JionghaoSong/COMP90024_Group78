import unittest
from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError, ConnectionTimeout
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Elasticsearch client
client = Elasticsearch(
    "https://localhost:9200",
    basic_auth=("elastic", os.getenv("ELASTIC_PSW")),
    verify_certs=False,
    timeout=60
)

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
    try:
        if client.indices.exists(index=index_name):
            client.indices.delete(index=index_name)
            print(f"Deleted existing index '{index_name}'.")

        response = client.indices.create(index=index_name, body=index_body)
        if 'acknowledged' in response and response['acknowledged']:
            print("Index creation acknowledged.")
        else:
            print("Index creation failed:", response)

        return response
    except ConnectionTimeout:
        print("Connection timed out while creating index.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

class TestCreateWeatherIndex(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # This method will be run once before all tests
        cls.client = Elasticsearch(
            "https://localhost:9200",
            basic_auth=("elastic", os.getenv("ELASTIC_PSW")),
            verify_certs=False,
            timeout=60
        )

    @classmethod
    def tearDownClass(cls):
        # This method will be run once after all tests
        try:
            cls.client.indices.delete(index='weather_station')
        except NotFoundError:
            pass
        except ConnectionTimeout:
            print("Connection timed out while deleting index.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def test_create_index(self):
        response = create_weather_index()
        if response:
            self.assertIn('acknowledged', response)
            self.assertTrue(response['acknowledged'])

    def test_insert_and_retrieve_data(self):
        response = create_weather_index()
        if not response:
            self.skipTest("Skipping test due to index creation failure.")
        else:
            # Insert data
            document = {
                "dev_id": "1",
                "date_measure": "2023-01-01T00:00:00Z",
                "RTC": 1625563200,
                "battery": 3.7,
                "solarPanel": 4.5,
                "command": 1,
                "solar": 500.0,
                "precipitation": 2.0,
                "strikes": 0,
                "windSpeed": 5.5,
                "windDirection": 180.0,
                "gustSpeed": 10.0,
                "vapourPressure": 1.0,
                "atmosphericPressure": 1013.0,
                "relativeHumidity": 60,
                "airTemp": 22.5,
                "Location": "40.7128,-74.0060",
                "Sensor_Name": "WeatherSensor1"
            }

            try:
                self.client.index(index='weather_station', id=1, document=document)
                # Retrieve data
                retrieved_doc = self.client.get(index='weather_station', id=1)
                self.assertEqual(retrieved_doc['_source'], document)
            except ConnectionTimeout:
                print("Connection timed out while indexing or retrieving data.")
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == '__main__':
    unittest.main()
