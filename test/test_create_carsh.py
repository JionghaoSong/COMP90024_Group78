import unittest
from unittest.mock import patch, MagicMock
from my_module import create_accident_index  # Replace 'my_module' with the actual module name

class TestCreateAccidentIndex(unittest.TestCase):

    @patch('my_module.client')
    def test_create_accident_index_success(self, mock_client):
        # Set up the mock client behavior
        mock_client.indices.exists.return_value = True
        mock_client.indices.delete.return_value = None
        mock_client.indices.create.return_value = {'acknowledged': True}

        # Call the function
        response = create_accident_index()

        # Assertions
        mock_client.indices.exists.assert_called_once_with(index='accidents')
        mock_client.indices.delete.assert_called_once_with(index='accidents')
        mock_client.indices.create.assert_called_once_with(index='accidents', body={
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
        })
        self.assertEqual(response, {'acknowledged': True})

    @patch('my_module.client')
    def test_create_accident_index_no_existing_index(self, mock_client):
        # Set up the mock client behavior
        mock_client.indices.exists.return_value = False
        mock_client.indices.create.return_value = {'acknowledged': True}

        # Call the function
        response = create_accident_index()

        # Assertions
        mock_client.indices.exists.assert_called_once_with(index='accidents')
        mock_client.indices.delete.assert_not_called()
        mock_client.indices.create.assert_called_once_with(index='accidents', body={
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
        })
        self.assertEqual(response, {'acknowledged': True})

    @patch('my_module.client')
    def test_create_accident_index_failure(self, mock_client):
        # Set up the mock client behavior
        mock_client.indices.exists.return_value = False
        mock_client.indices.create.return_value = {'acknowledged': False}

        # Call the function
        response = create_accident_index()

        # Assertions
        mock_client.indices.exists.assert_called_once_with(index='accidents')
        mock_client.indices.delete.assert_not_called()
        mock_client.indices.create.assert_called_once_with(index='accidents', body={
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
        })
        self.assertEqual(response, {'acknowledged': False})

