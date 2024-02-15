import unittest

import Project.Data.game_records
from Project.MTG_elements.auto_game import Game
import pandas as pd


class TestGame(unittest.TestCase):
    def setUp(self):
        self.mock_deck = pd.DataFrame({
            'card_slot': [1, 2, 3, 4, 5, 6, 7],
            'iscommander': [1, 0, 0, 0, 0, 0, 0],
            'island': [0, 0, 0, 1, 0, 1, 0],
            'mana_cost': [2, 3, 1, 0, 4, 0, 2],
            'mana_value': [0, 0, 0, 1, 0, 1, 0]
        })
        self.mock_game = Game(self.mock_deck)

    def test_cast_spells(self):
        initial_hand_count = len(self.mock_game.hand)
        self.mock_game.cast_spells()
        self.assertTrue(len(self.mock_game.hand) < initial_hand_count)
        self.assertTrue(len(self.mock_game.battlefield) > 0)
        self.assertTrue([2] in self.mock_game.battlefield['card_slot'].values)
        self.assertTrue([3] in self.mock_game.battlefield['card_slot'].values)
        self.assertFalse([4] in self.mock_game.battlefield['card_slot'].values)
        self.assertFalse([2] in self.mock_game.hand['card_slot'].values)
        self.assertFalse([3] in self.mock_game.hand['card_slot'].values)
        self.assertTrue([4] in self.mock_game.hand['card_slot'].values)
        self.assertTrue(self.mock_game.hand.index.is_monotonic_increasing)
        self.assertTrue(self.mock_game.battlefield.index.is_monotonic_increasing)


if __name__ == '__main__':
    unittest.main()
