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
        result = len(df[df['iscommander'] == 1])
        self.assertLessEqual(result, 2)
        self.assertNotEqual(result, 3)

    def test_lands_cost_zero_mana(self):
        land_df = self.df[self.df['island'] == 1]
        result = sum(land_df['mana_cost'])
        self.assertEqual(result, 0)

    def test_sumOther_isLess(self):
        commander_count = len(self.df[self.df['iscommander'] == 1])
        land_count = len(self.df[self.df['island'] == 1])
        ramp_count = len(self.df[self.df['isramp'] == 1])
        key_count = len(self.df[self.df['iskey'] == 1])
        kind_count = commander_count + land_count + ramp_count + key_count
        nokind_df = self.df[
            (self.df['iscommander'] == 0) &
            (self.df['island'] == 0) &
            (self.df['isramp'] == 0) &
            (self.df['iskey'] == 0)
            ]
        nokind_count = len(nokind_df)
        self.assertGreaterEqual(kind_count + nokind_count, 100)


if __name__ == '__main__':
    unittest.main()
