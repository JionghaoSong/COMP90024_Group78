import unittest
from unittest.mock import patch, MagicMock
from your_module import create_weather_index  # Replace 'your_module' with the actual module name

class TestCreateWeatherIndex(unittest.TestCase):

    @patch('your_module.client')
    def test_create_weather_index_success(self, mock_client):
        # Set up the mock client behavior
        mock_client.indices.exists.return_value = True
        mock_client.indices.delete.return_value = None
        mock_client.indices.create.return_value = {'acknowledged': True}

        # Call the function
        response = create_weather_index()

        # Assertions
        mock_client.indices.exists.assert_called_once_with(index='weather_station')
        mock_client.indices.delete.assert_called_once_with(index='weather_station')
        mock_client.indices.create.assert_called_once_with(index='weather_station', body={
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
        })
        self.assertEqual(response, {'acknowledged': True})

    @patch('your_module.client')
    def test_create_weather_index_no_existing_index(self, mock_client):
        # Set up the mock client behavior
        mock_client.indices.exists.return_value = False
        mock_client.indices.create.return_value = {'acknowledged': True}

        # Call the function
        response = create_weather_index()

        # Assertions
        mock_client.indices.exists.assert_called_once_with(index='weather_station')
        mock_client.indices.delete.assert_not_called()
        mock_client.indices.create.assert_called_once_with(index='weather_station', body={
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
        })
        self.assertEqual(response, {'acknowledged': True})

    @patch('your_module.client')
    def test_create_weather_index_failure(self, mock_client):
        # Set up the mock client behavior
        mock_client.indices.exists.return_value = False
        mock_client.indices.create.return_value = {'acknowledged': False}

        # Call the function
        response = create_weather_index()

        # Assertions
        mock_client.indices.exists.assert_called_once_with(index='weather_station')
        mock_client.indices.delete.assert_not_called()
        mock_client.indices.create.assert_called_once_with(index='weather_station', body={
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
        })
        self.assertEqual(response, {'acknowledged': False})

