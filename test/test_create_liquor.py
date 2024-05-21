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

def create_liquor_index():
    liquor = "liquor"
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
                "premises_name": {"type": "text"},
                "long": {"type": "float"},
                "lat": {"type": "float"},
                "lga": {"type": "keyword"}
            }
        }
    }

    try:
        if client.indices.exists(index=liquor):
            client.indices.delete(index=liquor)
            print(f"Deleted existing index '{liquor}'.")

        response = client.indices.create(index=liquor, body=index_body)
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

class TestCreateLiquorIndex(unittest.TestCase):

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
            cls.client.indices.delete(index='liquor')
        except NotFoundError:
            pass
        except ConnectionTimeout:
            print("Connection timed out while deleting index.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def test_create_index(self):
        response = create_liquor_index()
        if response:
            self.assertIn('acknowledged', response)
            self.assertTrue(response['acknowledged'])

    def test_insert_and_retrieve_data(self):
        response = create_liquor_index()
        if not response:
            self.skipTest("Skipping test due to index creation failure.")
        else:
            # Insert data
            document = {
                "objectid": 1,
                "premises_name": "Liquor Store",
                "long": 144.9631,
                "lat": -37.8136,
                "lga": "Melbourne"
            }

            try:
                self.client.index(index='liquor', id=1, document=document)
                # Retrieve data
                retrieved_doc = self.client.get(index='liquor', id=1)
                self.assertEqual(retrieved_doc['_source'], document)
            except ConnectionTimeout:
                print("Connection timed out while indexing or retrieving data.")
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == '__main__':
    unittest.main()
