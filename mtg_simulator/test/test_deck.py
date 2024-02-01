import unittest
import pandas as pd
from mtg.deck import deck_size, num_land


class TestDeck(unittest.TestCase):

    def setUp(self):
        self.cards_in_deck = pd.DataFrame({'card_slot': [1, 99, 45]})
        self.lands_in_deck = pd.DataFrame({'island': [0, 1, 1, 0, 0]})

    def test_deck_length(self):
        result = deck_size(self.cards_in_deck)
        self.assertEqual(result, 99, "deck size test failed")

    def test_num_land(self):
        result = num_land(self.lands_in_deck)
        self.assertEqual(result, 2, "land count test failed")


if __name__ == '__main__':
    unittest.main()
