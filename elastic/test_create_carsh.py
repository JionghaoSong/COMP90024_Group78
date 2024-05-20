import os
import unittest
from unittest.mock import patch, MagicMock
from create_crash import create_accident_index


class TestCreateAccidentIndex(unittest.TestCase):

    @patch('create_crash.Elasticsearch')
    def test_create_accident_index_success(self, mock_elasticsearch):
        # Mock the behavior of the Elasticsearch client
        mock_client = MagicMock()
        mock_client.indices.exists.return_value = False
        mock_client.indices.create.return_value = {'acknowledged': True}
        mock_elasticsearch.return_value = mock_client

        # Call the function
        response = create_accident_index()

        # Assertions
        mock_elasticsearch.assert_called_once_with(
            "https://localhost:9200",
            basic_auth=("elastic", os.getenv("ELASTIC_PSW")),
            verify_certs=False
        )
        mock_client.indices.exists.assert_called_once_with(index='accidents')
        mock_client.indices.delete.assert_not_called()
        mock_client.indices.create.assert_called_once()

        self.assertEqual(response, {'acknowledged': True})

    @patch('your_module.Elasticsearch')
    def test_create_accident_index_existing_index(self, mock_elasticsearch):
        # Mock the behavior of the Elasticsearch client
        mock_client = MagicMock()
        mock_client.indices.exists.return_value = True
        mock_client.indices.delete.return_value = None
        mock_client.indices.create.return_value = {'acknowledged': True}
        mock_elasticsearch.return_value = mock_client

        # Call the function
        response = create_accident_index()

        # Assertions
        mock_elasticsearch.assert_called_once_with(
            "https://localhost:9200",
            basic_auth=("elastic", os.getenv("ELASTIC_PSW")),
            verify_certs=False
        )
        mock_client.indices.exists.assert_called_once_with(index='accidents')
        mock_client.indices.delete.assert_called_once_with(index='accidents')
        mock_client.indices.create.assert_called_once()

        self.assertEqual(response, {'acknowledged': True})

    @patch('your_module.Elasticsearch')
    def test_create_accident_index_failure(self, mock_elasticsearch):
        # Mock the behavior of the Elasticsearch client
        mock_client = MagicMock()
        mock_client.indices.exists.return_value = False
        mock_client.indices.delete.return_value = None
        mock_client.indices.create.return_value = {'acknowledged': False}
        mock_elasticsearch.return_value = mock_client

        # Call the function
        response = create_accident_index()

        # Assertions
        mock_elasticsearch.assert_called_once_with(
            "https://localhost:9200",
            basic_auth=("elastic", os.getenv("ELASTIC_PSW")),
            verify_certs=False
        )
        mock_client.indices.exists.assert_called_once_with(index='accidents')
        mock_client.indices.delete.assert_not_called()
        mock_client.indices.create.assert_called_once()

        self.assertEqual(response, {'acknowledged': False})

if __name__ == '__main__':
    unittest.main()
