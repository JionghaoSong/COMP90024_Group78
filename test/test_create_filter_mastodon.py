import unittest
from unittest.mock import patch, MagicMock
from elasticsearch import Elasticsearch


from create_filter_mastodon import create_melbourne_mastodon_social_index

class TestCreateMelbourneMastodonSocialIndex(unittest.TestCase):

    @patch('elasticsearch.Elasticsearch')
    def test_create_index(self, mock_elasticsearch):
        # Mock Elasticsearch client
        mock_client = MagicMock()
        mock_elasticsearch.return_value = mock_client

        # Configure the mock responses
        mock_client.indices.exists.return_value = False  # Simulate index does not exist
        mock_client.indices.create.return_value = {'acknowledged': True}

        # Call the function
        response = create_melbourne_mastodon_social_index()

        # Assertions
        mock_client.indices.exists.assert_called_once_with(index='melbourne_mastodon_social')
        mock_client.indices.create.assert_called_once_with(index='melbourne_mastodon_social', body=unittest.mock.ANY)
        self.assertIn('acknowledged', response)
        self.assertTrue(response['acknowledged'])

    @patch('elasticsearch.Elasticsearch')
    def test_create_index_already_exists(self, mock_elasticsearch):
        # Mock Elasticsearch client
        mock_client = MagicMock()
        mock_elasticsearch.return_value = mock_client

        # Configure the mock responses
        mock_client.indices.exists.return_value = True  # Simulate index exists
        mock_client.indices.delete.return_value = {'acknowledged': True}
        mock_client.indices.create.return_value = {'acknowledged': True}

        # Call the function
        response = create_melbourne_mastodon_social_index()

        # Assertions
        mock_client.indices.exists.assert_called_once_with(index='melbourne_mastodon_social')
        mock_client.indices.delete.assert_called_once_with(index='melbourne_mastodon_social')
        mock_client.indices.create.assert_called_once_with(index='melbourne_mastodon_social', body=unittest.mock.ANY)
        self.assertIn('acknowledged', response)
        self.assertTrue(response['acknowledged'])

    @patch('elasticsearch.Elasticsearch')
    def test_create_index_failure(self, mock_elasticsearch):
        # Mock Elasticsearch client
        mock_client = MagicMock()
        mock_elasticsearch.return_value = mock_client

        # Configure the mock responses
        mock_client.indices.exists.return_value = False  # Simulate index does not exist
        mock_client.indices.create.return_value = {'acknowledged': False}

        # Call the function
        response = create_melbourne_mastodon_social_index()

        # Assertions
        mock_client.indices.exists.assert_called_once_with(index='melbourne_mastodon_social')
        mock_client.indices.create.assert_called_once_with(index='melbourne_mastodon_social', body=unittest.mock.ANY)
        self.assertIn('acknowledged', response)
        self.assertFalse(response['acknowledged'])

if __name__ == '__main__':
    unittest.main()
