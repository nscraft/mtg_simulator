import unittest
from unittest.mock import patch, mock_open
import pandas as pd
from Project.Data.deck_loader import DeckExcelMethod


class TestDeckExcelMethod(unittest.TestCase):
    @patch('deck_loader.pd.read_excel')
    @patch('deck_loader.os.path.join')
    @patch('deck_loader.os.path.dirname')
    def test_load_deck_excel(self, mock_dirname, mock_join, mock_read_excel):
        mock_dirname.return_value = '/fake/directory'
        mock_join.return_value = '/fake/directory/fake_deck.xlsx'
        mock_df = pd.DataFrame({'column1': [1, 2], 'column2': [3, 4]})
        mock_read_excel.return_value = mock_df
        deck_method = DeckExcelMethod('deck_sample.xlsx')
        result_df = deck_method.load_deck_excel()
        mock_dirname.assert_called_once_with(__file__)
        mock_join.assert_called_once_with('/fake/directory', 'fake_deck.xlsx')
        mock_read_excel.assert_called_once_with('/fake/directory/fake_deck.xlsx')
        pd.testing.assert_frame_equal(result_df, mock_df)


if __name__ == '__main__':
    unittest.main()

