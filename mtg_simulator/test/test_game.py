import unittest
import pandas as pd
from mtg.game import pick_card, island, GoldfishGame


class TestCardPicker(unittest.TestCase):

    def setUp(self):
        self.pool = [1, 2, 3, 4]
        self.cards = 2

    def test_pick_card_returns_correct_number_of_cards(self):
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


class TestGoldfishGame(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sample_data = {
            'card_slot': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        }
        cls.deck_df = pd.DataFrame(cls.sample_data)

    def setUp(self):
        self.game = GoldfishGame(TestGoldfishGame.deck_df)

    def test_draw_card(self):
        # Test drawing cards reduces the library size and increases hand size correctly
        self.game.draw_cards(5)
        self.assertEqual(len(self.game.hand), 5)
        self.assertEqual(len(self.game.library), 5)

        # Test drawing more cards than in the library raises an error
        with self.assertRaises(ValueError):
            self.game.draw_cards(6)

    def test_discard_cards(self):
        # Setup - Draw some cards first
        self.game.draw_cards(5)

        # Test discarding cards moves them from hand to graveyard
        cards_to_discard = {1, 2}
        self.game.discard_cards(cards_to_discard)
        self.assertEqual(self.game.hand, {3, 4, 5})
        self.assertEqual(self.game.graveyard, {1, 2})

        # Test discarding cards not in hand raises an error
        with self.assertRaises(ValueError):
            self.game.discard_cards({6})

    def test_discard_hand(self):
        # Setup - Draw some cards first
        self.game.draw_card(7)

        # Test discarding the entire hand
        self.game.discard_hand()
        self.assertEqual(len(self.game.hand), 0)
        self.assertEqual(len(self.game.graveyard), 7)


if __name__ == '__main__':
    unittest.main()
