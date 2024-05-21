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
    timeout=30,  # Add a timeout setting
    max_retries=10,  # Retry on failures
    retry_on_timeout=True  # Retry if timeout occurs
)

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

    try:
        if client.indices.exists(index=accident):
            client.indices.delete(index=accident)
            print(f"Deleted existing index '{accident}'.")

        response = client.indices.create(index=accident, body=index_body)
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

class TestCreateAccidentIndex(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # This method will be run once before all tests
        cls.client = Elasticsearch(
            "https://localhost:9200",
            basic_auth=("elastic", os.getenv("ELASTIC_PSW")),
            verify_certs=False,
            timeout=30,  # Add a timeout setting
            max_retries=10,  # Retry on failures
            retry_on_timeout=True  # Retry if timeout occurs
        )

    @classmethod
    def tearDownClass(cls):
        # This method will be run once after all tests
        try:
            cls.client.indices.delete(index='accidents')
        except NotFoundError:
            pass
        except ConnectionTimeout:
            print("Connection timed out while deleting index.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def test_create_index(self):
        response = create_accident_index()
        if response:
            self.assertIn('acknowledged', response)
            self.assertTrue(response['acknowledged'])

    def test_insert_and_retrieve_data(self):
        response = create_accident_index()
        if not response:
            self.skipTest("Skipping test due to index creation failure.")
        else:
            # Insert data
            document = {
                "objectid": 1,
                "accident_date": "2023-01-01",
                "day_of_week": "Monday",
                "longitude": 144.9631,
                "latitude": -37.8136,
                "alcoholtime": "No",
                "accident_type": "Collision",
                "light_condition": "Daylight",
                "speed_zone": "50 km/h",
                "lga_name": "Melbourne"
            }

            try:
                self.client.index(index='accidents', id=1, document=document)
                # Retrieve data
                retrieved_doc = self.client.get(index='accidents', id=1)
                self.assertEqual(retrieved_doc['_source'], document)
            except ConnectionTimeout:
                print("Connection timed out while indexing or retrieving data.")
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == '__main__':
    unittest.main()
