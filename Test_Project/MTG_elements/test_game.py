import unittest
import pandas as pd
from Project.MTG_elements.game import Game


class TestGameDrawCards(unittest.TestCase):

    def setUp(self):
        self.deck_df = pd.DataFrame({
            'card_slot': range(1, 101),
            'iscommander': [0] * 100,
            'island': [0, 1] * 50,
            'mana_cost': [1] * 100,
            'isramp': [1] * 100,
            'mana_value': [1] * 100,
            'isdraw': [1] * 100,
            'draw_value': [1] * 100,
            'card_score': [1] * 100
        })

        self.game = Game(self.deck_df)

    def test_draw_cards(self):
        self.game.draw_cards(7)
        self.assertEqual(len(self.game.hand), 7)
        self.assertEqual(len(self.game.library), 93)
        self.game.draw_cards(1)
        self.assertEqual(len(self.game.hand), 8)
        self.assertEqual(len(self.game.library), 92)

    def test_play_land(self):
        self.game.hand = pd.DataFrame({
            'card_slot': [1, 2, 3],
            'iscommander': [0, 0, 0],
            'island': [0, 1, 0],
            'mana_cost': [0, 0, 0],
            'isramp': [0, 0, 0],
            'mana_value': [0, 1, 0],
            'isdraw': [0, 0, 0],
            'draw_value': [0, 0, 0],
            'card_score': [0, 0, 0]
        })
        self.assertEqual(self.game.battlefield['card_slot'].tolist(), 2)


if __name__ == '__main__':
    unittest.main()
