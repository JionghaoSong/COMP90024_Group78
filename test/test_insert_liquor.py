import unittest
from unittest.mock import patch, mock_open, MagicMock
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import csv
import os
import uuid
from dotenv import load_dotenv

# Assume the function is in a module named liquor_data_module
from liquor_data_module import insert_liquor_data

class TestInsertLiquorData(unittest.TestCase):
    
    @patch('builtins.open', new_callable=mock_open, read_data='''objectid,premises_name,long,lat,lga
1,Venue A,144.9631,-37.8136,LGA1
2,Venue B,144.964,-37.814,LGA2
''')
    @patch('elasticsearch.Elasticsearch')
    @patch('elasticsearch.helpers.bulk')
    def test_insert_liquor_data(self, mock_bulk, mock_es, mock_open):
        # Mock Elasticsearch client
        mock_client = MagicMock()
        mock_es.return_value = mock_client
        
        # Run the function
        insert_liquor_data('dummy_path.csv', batch_size=2)

        # Check if bulk was called with the correct parameters
        self.assertTrue(mock_bulk.called)
        actions = mock_bulk.call_args[0][1]
        self.assertEqual(len(actions), 2)
        
        # Check the structure of the actions
        for action in actions:
            self.assertIn('_index', action)
            self.assertEqual(action['_index'], 'liquor')
            self.assertIn('_id', action)
            self.assertIn('_source', action)
            source = action['_source']
            self.assertIn('objectid', source)
            self.assertIn('premises_name', source)
            self.assertIn('long', source)
            self.assertIn('lat', source)
            self.assertIn('lga', source)

    @patch('builtins.open', new_callable=mock_open, read_data='''objectid,premises_name,long,lat,lga
1,Venue A,144.9631,-37.8136,LGA1
''')
    @patch('elasticsearch.Elasticsearch')
    @patch('elasticsearch.helpers.bulk')
    def test_insert_liquor_data_with_bulk_error(self, mock_bulk, mock_es, mock_open):
        # Mock Elasticsearch client
        mock_client = MagicMock()
        mock_es.return_value = mock_client
        
        # Configure bulk to raise an exception
        mock_bulk.side_effect = Exception('Bulk error')

        # Run the function and capture output
        with self.assertRaises(Exception):
            insert_liquor_data('dummy_path.csv', batch_size=1)

        # Ensure the bulk call was attempted
        self.assertTrue(mock_bulk.called)

if __name__ == '__main__':
    unittest.main()
