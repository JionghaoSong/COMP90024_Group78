import unittest
from unittest.mock import patch, MagicMock
from your_module import insert_accident_data  # Replace 'your_module' with the actual module name

class TestInsertAccidentData(unittest.TestCase):

    @patch('your_module.open')
    @patch('your_module.csv.DictReader')
    @patch('your_module.bulk')
    def test_insert_accident_data_success(self, mock_bulk, mock_reader, mock_open):
        # Set up mock behavior
        mock_file = MagicMock()
        mock_open.return_value.__enter__.return_value = mock_file
        mock_reader_instance = MagicMock()
        mock_reader_instance.fieldnames = [
            "OBJECTID", "ACCIDENT_DATE", "DAY_OF_WEEK", "LONGITUDE", "LATITUDE", "ALCOHOLTIME",
            "ACCIDENT_TYPE", "LIGHT_CONDITION", "SPEED_ZONE", "LGA_NAME"
        ]
        mock_reader.return_value = mock_reader_instance
        mock_bulk.return_value = None

        # Call the function
        insert_accident_data('test_data.csv')

        # Assertions
        mock_open.assert_called_once_with('test_data.csv', 'r', encoding='utf-8-sig')
        mock_reader.assert_called_once_with(mock_file)
        mock_bulk.assert_called()  # Ensure bulk insert is called

    @patch('your_module.open')
    @patch('your_module.csv.DictReader')
    @patch('your_module.bulk')
    def test_insert_accident_data_bulk_error(self, mock_bulk, mock_reader, mock_open):
        # Set up mock behavior
        mock_file = MagicMock()
        mock_open.return_value.__enter__.return_value = mock_file
        mock_reader_instance = MagicMock()
        mock_reader_instance.fieldnames = [
            "OBJECTID", "ACCIDENT_DATE", "DAY_OF_WEEK", "LONGITUDE", "LATITUDE", "ALCOHOLTIME",
            "ACCIDENT_TYPE", "LIGHT_CONDITION", "SPEED_ZONE", "LGA_NAME"
        ]
        mock_reader.return_value = mock_reader_instance
        mock_bulk.side_effect = Exception("Bulk insert error")

        # Call the function
        insert_accident_data('test_data.csv')

        # Assertions
        mock_open.assert_called_once_with('test_data.csv', 'r', encoding='utf-8-sig')
        mock_reader.assert_called_once_with(mock_file)
        mock_bulk.assert_called()  # Ensure bulk insert is called

