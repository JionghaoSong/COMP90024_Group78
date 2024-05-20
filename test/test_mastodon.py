import unittest
from unittest.mock import patch, MagicMock
from your_module import create_mastodon_social_index  # Replace 'your_module' with the actual module name

class TestCreateMastodonSocialIndex(unittest.TestCase):

    @patch('your_module.client')
    def test_create_mastodon_social_index_success(self, mock_client):
        # Set up the mock client behavior
        mock_client.indices.exists.return_value = True
        mock_client.indices.delete.return_value = None
        mock_client.indices.create.return_value = {'acknowledged': True}

        # Call the function
        response = create_mastodon_social_index()

        # Assertions
        mock_client.indices.exists.assert_called_once_with(index='mastodon_social')
        mock_client.indices.delete.assert_called_once_with(index='mastodon_social')
        mock_client.indices.create.assert_called_once_with(index='mastodon_social', body={
            "settings": {
                "index": {
                    "number_of_shards": 3,
                    "number_of_replicas": 1
                }
            },
            "mappings": {
                "properties": {
                    "id": {"type": "keyword"},
                    "created_at": {"type": "date"},
                    "lang": {"type": "keyword"},
                    "sentiment": {"type": "float"},
                    "tokens": {"type": "text"},
                    "tags": {"type": "keyword"}
                }
            }
        })
        self.assertEqual(response, {'acknowledged': True})

    @patch('your_module.client')
    def test_create_mastodon_social_index_no_existing_index(self, mock_client):
        # Set up the mock client behavior
        mock_client.indices.exists.return_value = False
        mock_client.indices.create.return_value = {'acknowledged': True}

        # Call the function
        response = create_mastodon_social_index()

        # Assertions
        mock_client.indices.exists.assert_called_once_with(index='mastodon_social')
        mock_client.indices.delete.assert_not_called()
        mock_client.indices.create.assert_called_once_with(index='mastodon_social', body={
            "settings": {
                "index": {
                    "number_of_shards": 3,
                    "number_of_replicas": 1
                }
            },
            "mappings": {
                "properties": {
                    "id": {"type": "keyword"},
                    "created_at": {"type": "date"},
                    "lang": {"type": "keyword"},
                    "sentiment": {"type": "float"},
                    "tokens": {"type": "text"},
                    "tags": {"type": "keyword"}
                }
            }
        })
        self.assertEqual(response, {'acknowledged': True})

    @patch('your_module.client')
    def test_create_mastodon_social_index_failure(self, mock_client):
        # Set up the mock client behavior
        mock_client.indices.exists.return_value = False
        mock_client.indices.create.return_value = {'acknowledged': False}

        # Call the function
        response = create_mastodon_social_index()

        # Assertions
        mock_client.indices.exists.assert_called_once_with(index='mastodon_social')
        mock_client.indices.delete.assert_not_called()
        mock_client.indices.create.assert_called_once_with(index='mastodon_social', body={
            "settings": {
                "index": {
                    "number_of_shards": 3,
                    "number_of_replicas": 1
                }
            },
            "mappings": {
                "properties": {
                    "id": {"type": "keyword"},
                    "created_at": {"type": "date"},
                    "lang": {"type": "keyword"},
                    "sentiment": {"type": "float"},
                    "tokens": {"type": "text"},
                    "tags": {"type": "keyword"}
                }
            }
        })
        self.assertEqual(response, {'acknowledged': False})

if __name__ == '__main__':
    unittest.main()
