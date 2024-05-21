import unittest
from unittest.mock import patch, mock_open, MagicMock
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import csv
import os
from dotenv import load_dotenv

# Assume the function is in a module named weather_data_module
from weather_data_module import insert_weather_station_data

class TestInsertWeatherStationData(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='''dev_id,date_measure,RTC,battery,solarPanel,command,solar,precipitation,strikes,windSpeed,windDirection,gustSpeed,vapourPressure,atmosphericPressure,relativeHumidity,airTemp,Lat Long,Sensor Name
1,2023-05-01,1622563200,4.2,3.6,1,1.5,0.0,0,5.2,180,7.4,0.9,1013.1,60,22.5,-37.8136,144.9631,Sensor A
2,2023-05-01,1622566800,4.1,3.5,1,1.4,0.0,0,5.1,175,7.3,0.8,1012.9,59,22.1,-37.814,144.964,Sensor B
''')
    @patch('elasticsearch.Elasticsearch')
    @patch('elasticsearch.helpers.bulk')
    def test_insert_weather_station_data(self, mock_bulk, mock_es, mock_open):
        # Mock Elasticsearch client
        mock_client = MagicMock()
        mock_es.return_value = mock_client

        # Run the function
        insert_weather_station_data('dummy_path.csv', batch_size=2)

        # Check if bulk was called with the correct parameters
        self.assertTrue(mock_bulk.called)
        actions = mock_bulk.call_args[0][1]
        self.assertEqual(len(actions), 2)

        # Check the structure of the actions
        for action in actions:
            self.assertIn('_index', action)
            self.assertEqual(action['_index'], 'weather_station')
            self.assertIn('_id', action)
            self.assertIn('_source', action)
            source = action['_source']
            self.assertIn('dev_id', source)
            self.assertIn('date_measure', source)
            self.assertIn('RTC', source)
            self.assertIn('battery', source)
            self.assertIn('solarPanel', source)
            self.assertIn('command', source)
            self.assertIn('solar', source)
            self.assertIn('precipitation', source)
            self.assertIn('strikes', source)
            self.assertIn('windSpeed', source)
            self.assertIn('windDirection', source)
            self.assertIn('gustSpeed', source)
            self.assertIn('vapourPressure', source)
            self.assertIn('atmosphericPressure', source)
            self.assertIn('relativeHumidity', source)
            self.assertIn('airTemp', source)
            self.assertIn('Location', source)
            location = source['Location']
            if location:
                self.assertIn('lat', location)
                self.assertIn('lon', location)
            self.assertIn('Sensor_Name', source)

    @patch('builtins.open', new_callable=mock_open, read_data='''dev_id,date_measure,RTC,battery,solarPanel,command,solar,precipitation,strikes,windSpeed,windDirection,gustSpeed,vapourPressure,atmosphericPressure,relativeHumidity,airTemp,Lat Long,Sensor Name
1,2023-05-01,1622563200,4.2,3.6,1,1.5,0.0,0,5.2,180,7.4,0.9,1013.1,60,22.5,-37.8136,144.9631,Sensor A
''')
    @patch('elasticsearch.Elasticsearch')
    @patch('elasticsearch.helpers.bulk')
    def test_insert_weather_station_data_with_bulk_error(self, mock_bulk, mock_es, mock_open):
        # Mock Elasticsearch client
        mock_client = MagicMock()
        mock_es.return_value = mock_client

        # Configure bulk to raise an exception
        mock_bulk.side_effect = Exception('Bulk error')

        # Run the function and capture output
        with self.assertRaises(Exception):
            insert_weather_station_data('dummy_path.csv', batch_size=1)

        # Ensure the bulk call was attempted
        self.assertTrue(mock_bulk.called)

if __name__ == '__main__':
    unittest.main()
