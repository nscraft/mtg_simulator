import unittest
import pandas as pd
from Project.Events.goldfish import GoldfishGame


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
        self.game.draw_cards(5)
        self.assertEqual(len(self.game.hand), 5)
        self.assertEqual(len(self.game.library), 5)
        with self.assertRaises(ValueError):
            self.game.draw_cards(6)

    def test_discard_cards(self):
        self.game.draw_cards(10)
        cards_to_discard = {1, 2}
        self.game.discard_cards(cards_to_discard)
        self.assertEqual(self.game.hand, {3, 4, 5, 6, 7, 8, 9, 10})
        self.assertEqual(self.game.graveyard, {1, 2})

    def test_discard_hand(self):
        self.game.draw_cards(7)
        self.game.discard_hand()
        self.assertEqual(len(self.game.hand), 0)
        self.assertEqual(len(self.game.graveyard), 7)


if __name__ == '__main__':
    unittest.main()
