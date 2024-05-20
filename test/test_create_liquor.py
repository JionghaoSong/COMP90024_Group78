import unittest
from unittest.mock import patch, MagicMock
from your_module import create_liquor_index  # Replace 'your_module' with the actual module name

class TestCreateLiquorIndex(unittest.TestCase):

    @patch('your_module.client')
    def test_create_liquor_index_success(self, mock_client):
        # Set up the mock client behavior
        mock_client.indices.exists.return_value = True
        mock_client.indices.delete.return_value = None
        mock_client.indices.create.return_value = {'acknowledged': True}

        # Call the function
        response = create_liquor_index()

        # Assertions
        mock_client.indices.exists.assert_called_once_with(index='liquor')
        mock_client.indices.delete.assert_called_once_with(index='liquor')
        mock_client.indices.create.assert_called_once_with(index='liquor', body={
            "settings": {
                "index": {
                    "number_of_shards": 3,
                    "number_of_replicas": 1
                }
            },
            "mappings": {
                "properties": {
                    "premises_name": {"type": "text"},
                    "suburb": {"type": "keyword"},
                    "licence_no": {"type": "keyword"},
                    "address_1": {"type": "text"},
                    "address_2": {"type": "text"},
                    "postcode": {"type": "integer"},
                    "long": {"type": "float"},
                    "licence_category": {"type": "text"},
                    "objectid": {"type": "integer"},
                    "lga": {"type": "keyword"},
                    "lat": {"type": "float"}
                }
            }
        })
        self.assertEqual(response, {'acknowledged': True})

    @patch('your_module.client')
    def test_create_liquor_index_no_existing_index(self, mock_client):
        # Set up the mock client behavior
        mock_client.indices.exists.return_value = False
        mock_client.indices.create.return_value = {'acknowledged': True}

        # Call the function
        response = create_liquor_index()

        # Assertions
        mock_client.indices.exists.assert_called_once_with(index='liquor')
        mock_client.indices.delete.assert_not_called()
        mock_client.indices.create.assert_called_once_with(index='liquor', body={
            "settings": {
                "index": {
                    "number_of_shards": 3,
                    "number_of_replicas": 1
                }
            },
            "mappings": {
                "properties": {
                    "premises_name": {"type": "text"},
                    "suburb": {"type": "keyword"},
                    "licence_no": {"type": "keyword"},
                    "address_1": {"type": "text"},
                    "address_2": {"type": "text"},
                    "postcode": {"type": "integer"},
                    "long": {"type": "float"},
                    "licence_category": {"type": "text"},
                    "objectid": {"type": "integer"},
                    "lga": {"type": "keyword"},
                    "lat": {"type": "float"}
                }
            }
        })
        self.assertEqual(response, {'acknowledged': True})

    @patch('your_module.client')
    def test_create_liquor_index_failure(self, mock_client):
        # Set up the mock client behavior
        mock_client.indices.exists.return_value = False
        mock_client.indices.create.return_value = {'acknowledged': False}

        # Call the function
        response = create_liquor_index()

        # Assertions
        mock_client.indices.exists.assert_called_once_with(index='liquor')
        mock_client.indices.delete.assert_not_called()
        mock_client.indices.create.assert_called_once_with(index='liquor', body={
            "settings": {
                "index": {
                    "number_of_shards": 3,
                    "number_of_replicas": 1
                }
            },
            "mappings": {
                "properties": {
                    "premises_name": {"type": "text"},
                    "suburb": {"type": "keyword"},
                    "licence_no": {"type": "keyword"},
                    "address_1": {"type": "text"},
                    "address_2": {"type": "text"},
                    "postcode": {"type": "integer"},
                    "long": {"type": "float"},
                    "licence_category": {"type": "text"},
                    "objectid": {"type": "integer"},
                    "lga": {"type": "keyword"},
                    "lat": {"type": "float"}
                }
            }
        })
        self.assertEqual(response, {'acknowledged': False})

if __name__ == '__main__':
    unittest.main()
