import unittest
import pandas as pd
from Project.MTG_elements.auto_game_components import GameComponents


class TestGame(unittest.TestCase):
    def setUp(self):
        self.mock_deck = pd.DataFrame({
            'card_slot': [1, 2, 3, 4, 5, 6],
            'iscommander': [1, 0, 0, 0, 0, 0],
            'island': [0, 0, 0, 1, 0, 1],
            'mana_cost': [2, 3, 1, 0, 4, 0],
            'isramp': [0, 0, 1, 0, 0, 0],
            'mana_value': [0, 0, 0, 1, 0, 1],
            'isdraw': [0, 0, 1, 0, 0, 0],
            'draw_value': [0, 0, 2, 0, 0, 0],
            'card_score': [2, 3, 0, 0, 4, 0],

        })
        self.game = GameComponents(self.mock_deck)

    def test_cast_spells(self):
        self.game.hand = pd.DataFrame({
            'card_slot': [1, 2, 3, 4, 5, 6],
            'iscommander': [1, 0, 0, 0, 0, 0],
            'island': [0, 0, 0, 1, 0, 1],
            'mana_cost': [2, 3, 1, 0, 4, 0],
            'isramp': [0, 0, 1, 0, 0, 0],
            'mana_value': [0, 0, 0, 1, 0, 1],
            'isdraw': [0, 0, 1, 0, 0, 0],
            'draw_value': [0, 0, 2, 0, 0, 0],
            'card_score': [2, 3, 0, 0, 4, 0],

        })
        initial_hand_count = len(self.game.hand)
        self.game.total_mana = 5
        self.game.cast_spells()
        self.assertTrue(len(self.game.hand) < initial_hand_count)
        self.assertTrue(len(self.game.battlefield) > 0)


if __name__ == '__main__':
    unittest.main()
