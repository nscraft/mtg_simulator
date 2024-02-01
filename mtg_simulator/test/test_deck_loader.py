import unittest
import numpy as np
from data.deck_loader import write_deck, load_deck_excel, write_deck_withpartners


class TestWriteDeck(unittest.TestCase):

    def setUp(self):
        self.df = write_deck()

    def test_write_deck_not_empty(self):
        result = self.df
        self.assertIsNotNone(result)

    def test_deck_len(self):
        result = len(self.df)
        self.assertEqual(result, 100)

    def test_deck_commanders_notThree(self):
        df = self.df
        result = len(df['iscommander'])
        self.assertLessEqual(result, 2)
        self.assertNotEqual(result, 3)

    def test_sumLandsumOther_isDeck(self):


if __name__ == '__main__':
    unittest.main()
