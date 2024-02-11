import unittest
import pandas as pd
from Project.Analytics.deck_opener import deck_size, num_land, deck_library, avg_mana_cost, num_other


class TestDeck(unittest.TestCase):

    def setUp(self):
        self.test_deck = pd.DataFrame(
            {'card_slot': [1, 2, 3, 4, 100],
             'iscommander': [1, 0, 0, 0, 0],
             'island': [0, 1, 1, 0, 0],
             'isramp': [0, 0, 0, 1, 0],
             'ramp_value': [0, 0, 0, 2, 0],
             'iskey': [1, 0, 0, 0, 1],
             'key_value': [1, 1, 0, 0, 7],
             'mana_cost': [3, 0, 0, 1, 3]
             })

    def test_deck_length(self):
        result = deck_size(self.test_deck)
        self.assertEqual(result, 100, "deck size test failed")

    def test_deck_library(self):
        result = deck_library(self.test_deck)
        self.assertEqual(result, 4)

    def test_num_land(self):
        result = num_land(self.test_deck)
        self.assertEqual(result, 2, "land count test failed")

    def test_avg_mana_cost(self):
        result = avg_mana_cost(self.test_deck)
        self.assertEqual(result, 2.33)

    def test_num_other(self):
        result = num_other(self.test_deck)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
