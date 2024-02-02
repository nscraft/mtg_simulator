import unittest
import pandas as pd
from mtg.game import pick_card, island


class TestDeck(unittest.TestCase):

    def setUp(self):
        self.pool = [1, 2, 3, 4]
        self.cards = 2

    def test_pick_card(self):
        result = pick_card(self.pool, self.cards)
        count = len(result)
        self.assertIsNotNone(result)
        self.assertEqual(count, self.cards)
        self.assertTrue(all(card in self.pool for card in result))


class TestCardsInHand(unittest.TestCase):

    def setUp(self):
        self.deck_df = pd.DataFrame(
            {'card_slot': [1, 2, 3, 4, 5],
             'island': [0, 0, 1, 1, 0]})
        self.set = {2, 3}

    def test_island(self):
        result = island(self.deck_df, self.set)
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
