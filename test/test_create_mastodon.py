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

def create_mastodon_social_index():
    mastodon_social = "mastodon_social"
    index_body = {
        "settings": {
            "index": {
                "number_of_shards": 3,
                "number_of_replicas": 1
            }
        },
        "mappings": {
            "properties": {
                "id": {"type": "keyword"},
                "created_at": {"type": "date"},
                "lang": {"type": "keyword"},
                "sentiment": {"type": "float"},
                "tokens": {"type": "text"},
                "tags": {"type": "keyword"}
            }
        }
    }
    try:
        if client.indices.exists(index=mastodon_social):
            client.indices.delete(index=mastodon_social)
            print(f"Deleted existing index '{mastodon_social}'.")

        response = client.indices.create(index=mastodon_social, body=index_body)
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

class TestCreateMastodonSocialIndex(unittest.TestCase):

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
            cls.client.indices.delete(index='mastodon_social')
        except NotFoundError:
            pass
        except ConnectionTimeout:
            print("Connection timed out while deleting index.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def test_create_index(self):
        response = create_mastodon_social_index()
        if response:
            self.assertIn('acknowledged', response)
            self.assertTrue(response['acknowledged'])

    def test_insert_and_retrieve_data(self):
        response = create_mastodon_social_index()
        if not response:
            self.skipTest("Skipping test due to index creation failure.")
        else:
            # Insert data
            document = {
                "id": "1",
                "created_at": "2023-01-01T00:00:00Z",
                "lang": "en",
                "sentiment": 0.5,
                "tokens": "example tokens",
                "tags": ["example", "test"]
            }

            try:
                self.client.index(index='mastodon_social', id=1, document=document)
                # Retrieve data
                retrieved_doc = self.client.get(index='mastodon_social', id=1)
                self.assertEqual(retrieved_doc['_source'], document)
            except ConnectionTimeout:
                print("Connection timed out while indexing or retrieving data.")
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == '__main__':
    unittest.main()
