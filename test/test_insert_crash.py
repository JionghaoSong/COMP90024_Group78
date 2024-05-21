import unittest
from unittest.mock import patch, mock_open, MagicMock
from elasticsearch import Elasticsearch, TransportError
from elasticsearch.helpers import bulk, BulkIndexError
import os
import uuid
import csv

# Assume the function is in a module named accident_data_module
from accident_data_module import insert_accident_data

class TestInsertAccidentData(unittest.TestCase):
    
    @patch('builtins.open', new_callable=mock_open, read_data='''OBJECTID,ACCIDENT_DATE,DAY_OF_WEEK,LONGITUDE,LATITUDE,ALCOHOLTIME,ACCIDENT_TYPE,LIGHT_CONDITION,SPEED_ZONE,LGA_NAME
1,2021-01-01,Friday,144.9631,-37.8136,No,Hit pedestrian,Day,50,Melbourne
2,2021-01-02,Saturday,144.964,-37.814,No,Vehicle collision,Night,60,Port Phillip
''')
    @patch('elasticsearch.Elasticsearch')
    @patch('elasticsearch.helpers.bulk')
    def test_insert_accident_data(self, mock_bulk, mock_es, mock_open):
        # Mock Elasticsearch client
        mock_client = MagicMock()
        mock_es.return_value = mock_client
        
        # Run the function
        insert_accident_data('dummy_path.csv', batch_size=2)

        # Check if bulk was called with the correct parameters
        self.assertTrue(mock_bulk.called)
        actions = mock_bulk.call_args[0][1]
        self.assertEqual(len(actions), 2)
        
        # Check the structure of the actions
        for action in actions:
            self.assertIn('_index', action)
            self.assertEqual(action['_index'], 'accidents')
            self.assertIn('_id', action)
            self.assertIn('_source', action)
            source = action['_source']
            self.assertIn('objectid', source)
            self.assertIn('accident_date', source)
            self.assertIn('day_of_week', source)
            self.assertIn('longitude', source)
            self.assertIn('latitude', source)
            self.assertIn('alcoholtime', source)
            self.assertIn('accident_type', source)
            self.assertIn('light_condition', source)
            self.assertIn('speed_zone', source)
            self.assertIn('lga_name', source)

    @patch('builtins.open', new_callable=mock_open, read_data='''OBJECTID,ACCIDENT_DATE,DAY_OF_WEEK,LONGITUDE,LATITUDE,ALCOHOLTIME,ACCIDENT_TYPE,LIGHT_CONDITION,SPEED_ZONE,LGA_NAME
1,2021-01-01,Friday,144.9631,-37.8136,No,Hit pedestrian,Day,50,Melbourne
''')
    @patch('elasticsearch.Elasticsearch')
    @patch('elasticsearch.helpers.bulk')
    def test_insert_accident_data_with_bulk_error(self, mock_bulk, mock_es, mock_open):
        # Mock Elasticsearch client
        mock_client = MagicMock()
        mock_es.return_value = mock_client
        
        # Configure bulk to raise BulkIndexError
        mock_bulk.side_effect = BulkIndexError('Bulk error', [{'index': {'_id': '1', 'error': 'Some error'}}])

        # Run the function
        with self.assertRaises(BulkIndexError):
            insert_accident_data('dummy_path.csv', batch_size=1)

        # Ensure the bulk call was attempted
        self.assertTrue(mock_bulk.called)

if __name__ == '__main__':
    unittest.main()
