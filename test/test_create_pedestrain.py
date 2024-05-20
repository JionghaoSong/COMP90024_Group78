import unittest
from unittest.mock import patch, MagicMock
from your_module import create_pedestrian_index  # Replace 'your_module' with the actual module name

class TestCreatePedestrianIndex(unittest.TestCase):

    @patch('your_module.client')
    def test_create_pedestrian_index_success(self, mock_client):
        # Set up the mock client behavior
        mock_client.indices.exists.return_value = True
        mock_client.indices.delete.return_value = None
        mock_client.indices.create.return_value = {'acknowledged': True}

        # Call the function
        response = create_pedestrian_index()

        # Assertions
        mock_client.indices.exists.assert_called_once_with(index='ped_counting')
        mock_client.indices.delete.assert_called_once_with(index='ped_counting')
        mock_client.indices.create.assert_called_once_with(index='ped_counting', body={
            "settings": {
                "index": {
                    "number_of_shards": 3,
                    "number_of_replicas": 1
                }
            },
            "mappings": {
                "properties": {
                    "Sensor_Name": {"type": "text"},
                    "SensingDateTime(Hour)": {"type": "date"},
                    "LocationID": {"type": "integer"},
                    "Direction_1": {"type": "integer"},
                    "Direction_2": {"type": "integer"},
                    "Total_of_Directions": {"type": "integer"},
                    "Location": {"type": "geo_point"}
                }
            }
        })
        self.assertEqual(response, {'acknowledged': True})

    @patch('your_module.client')
    def test_create_pedestrian_index_no_existing_index(self, mock_client):
        # Set up the mock client behavior
        mock_client.indices.exists.return_value = False
        mock_client.indices.create.return_value = {'acknowledged': True}

        # Call the function
        response = create_pedestrian_index()

        # Assertions
        mock_client.indices.exists.assert_called_once_with(index='ped_counting')
        mock_client.indices.delete.assert_not_called()
        mock_client.indices.create.assert_called_once_with(index='ped_counting', body={
            "settings": {
                "index": {
                    "number_of_shards": 3,
                    "number_of_replicas": 1
                }
            },
            "mappings": {
                "properties": {
                    "Sensor_Name": {"type": "text"},
                    "SensingDateTime(Hour)": {"type": "date"},
                    "LocationID": {"type": "integer"},
                    "Direction_1": {"type": "integer"},
                    "Direction_2": {"type": "integer"},
                    "Total_of_Directions": {"type": "integer"},
                    "Location": {"type": "geo_point"}
                }
            }
        })
        self.assertEqual(response, {'acknowledged': True})

    @patch('your_module.client')
    def test_create_pedestrian_index_failure(self, mock_client):
        # Set up the mock client behavior
        mock_client.indices.exists.return_value = False
        mock_client.indices.create.return_value = {'acknowledged': False}

        # Call the function
        response = create_pedestrian_index()

        # Assertions
        mock_client.indices.exists.assert_called_once_with(index='ped_counting')
        mock_client.indices.delete.assert_not_called()
        mock_client.indices.create.assert_called_once_with(index='ped_counting', body={
            "settings": {
                "index": {
                    "number_of_shards": 3,
                    "number_of_replicas": 1
                }
            },
            "mappings": {
                "properties": {
                    "Sensor_Name": {"type": "text"},
                    "SensingDateTime(Hour)": {"type": "date"},
                    "LocationID": {"type": "integer"},
                    "Direction_1": {"type": "integer"},
                    "Direction_2": {"type": "integer"},
                    "Total_of_Directions": {"type": "integer"},
                    "Location": {"type": "geo_point"}
                }
            }
        })
        self.assertEqual(response, {'acknowledged': False})

