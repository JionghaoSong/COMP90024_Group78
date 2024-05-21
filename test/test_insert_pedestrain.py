import unittest
from unittest.mock import patch, mock_open, MagicMock
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import csv
import os
from dotenv import load_dotenv
import uuid

# Assume the function is in a module named ped_data_module
from ped_data_module import insert_ped_data

class TestInsertPedData(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='''LocationID,Sensor_Name,SensingDateTime(Hour),Direction_1,Direction_2,Total_of_Directions,Location
1,Sensor A,2023-05-01T00:00,5,10,15,-37.8136,144.9631
2,Sensor B,2023-05-01T01:00,3,6,9,-37.814,144.964
''')
    @patch('elasticsearch.Elasticsearch')
    @patch('elasticsearch.helpers.bulk')
    def test_insert_ped_data(self, mock_bulk, mock_es, mock_open):
        # Mock Elasticsearch client
        mock_client = MagicMock()
        mock_es.return_value = mock_client

        # Run the function
        insert_ped_data('dummy_path.csv', batch_size=2)

        # Check if bulk was called with the correct parameters
        self.assertTrue(mock_bulk.called)
        actions = mock_bulk.call_args[0][1]
        self.assertEqual(len(actions), 2)

        # Check the structure of the actions
        for action in actions:
            self.assertIn('_index', action)
            self.assertEqual(action['_index'], 'pes_counting')
            self.assertIn('_id', action)
            self.assertIn('_source', action)
            source = action['_source']
            self.assertIn('Sensor_Name', source)
            self.assertIn('SensingDateTime(Hour)', source)
            self.assertIn('LocationID', source)
            self.assertIn('Direction_1', source)
            self.assertIn('Direction_2', source)
            self.assertIn('Total_of_Directions', source)
            self.assertIn('Location', source)
            location = source['Location']
            self.assertIn('lat', location)
            self.assertIn('lon', location)

    @patch('builtins.open', new_callable=mock_open, read_data='''LocationID,Sensor_Name,SensingDateTime(Hour),Direction_1,Direction_2,Total_of_Directions,Location
1,Sensor A,2023-05-01T00:00,5,10,15,-37.8136,144.9631
''')
    @patch('elasticsearch.Elasticsearch')
    @patch('elasticsearch.helpers.bulk')
    def test_insert_ped_data_with_bulk_error(self, mock_bulk, mock_es, mock_open):
        # Mock Elasticsearch client
        mock_client = MagicMock()
        mock_es.return_value = mock_client

        # Configure bulk to raise an exception
        mock_bulk.side_effect = Exception('Bulk error')

        # Run the function and capture output
        with self.assertRaises(Exception):
            insert_ped_data('dummy_path.csv', batch_size=1)

        # Ensure the bulk call was attempted
        self.assertTrue(mock_bulk.called)

if __name__ == '__main__':
    unittest.main()
