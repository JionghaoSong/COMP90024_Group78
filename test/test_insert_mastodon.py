import unittest
from unittest.mock import patch, mock_open, MagicMock
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import json
import os
from dotenv import load_dotenv


from insert_mastodon import insert_mastodon_data

class TestInsertMastodonData(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='''{"id": "1", "created_at": "2023-01-01T00:00:00Z", "lang": "en", "sentiment": 0.5, "tokens": "example tokens", "tags": ["example", "test"]}
{"id": "2", "created_at": "2023-01-02T00:00:00Z", "lang": "en", "sentiment": 0.6, "tokens": "another example", "tags": ["example", "test"]}
''')
    @patch('elasticsearch.Elasticsearch')
    @patch('elasticsearch.helpers.bulk')
    def test_insert_mastodon_data(self, mock_bulk, mock_es, mock_open):
        # Mock Elasticsearch client
        mock_client = MagicMock()
        mock_es.return_value = mock_client
        
        # Run the function
        insert_mastodon_data('dummy_path.json', batch_size=2)

        # Check if bulk was called with the correct parameters
        self.assertTrue(mock_bulk.called)
        actions = mock_bulk.call_args[0][1]
        self.assertEqual(len(actions), 2)
        
        # Check the structure of the actions
        for action in actions:
            self.assertIn('_index', action)
            self.assertEqual(action['_index'], 'mastodon_social')
            self.assertIn('_id', action)
            self.assertIn('_source', action)
            source = action['_source']
            self.assertIn('id', source)
            self.assertIn('created_at', source)
            self.assertIn('lang', source)
            self.assertIn('sentiment', source)
            self.assertIn('tokens', source)
            self.assertIn('tags', source)

    @patch('builtins.open', new_callable=mock_open, read_data='''{"id": "1", "created_at": "2023-01-01T00:00:00Z", "lang": "en", "sentiment": 0.5, "tokens": "example tokens", "tags": ["example", "test"]}
''')
    @patch('elasticsearch.Elasticsearch')
    @patch('elasticsearch.helpers.bulk')
    def test_insert_mastodon_data_with_bulk_error(self, mock_bulk, mock_es, mock_open):
        # Mock Elasticsearch client
        mock_client = MagicMock()
        mock_es.return_value = mock_client
        
        # Configure bulk to raise an exception
        mock_bulk.side_effect = Exception('Bulk error')

        # Run the function and capture output
        with self.assertRaises(Exception):
            insert_mastodon_data('dummy_path.json', batch_size=1)

        # Ensure the bulk call was attempted
        self.assertTrue(mock_bulk.called)

if __name__ == '__main__':
    unittest.main()
