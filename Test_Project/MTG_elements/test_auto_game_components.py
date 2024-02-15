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
            'mana_value': [0, 0, 0, 1, 0, 1]
        })
        self.game = GameComponents(self.mock_deck)

    def test_cast_spells(self):
        self.game.total_mana = 5
        self.game.draw_cards(3)
        initial_hand_count = len(self.game.hand)
        self.game.cast_spells()
        self.assertTrue(len(self.game.hand) < initial_hand_count)
        self.assertTrue(len(self.game.battlefield) > 0)
        self.assertTrue([2] in self.game.battlefield['card_slot'].values)
        self.assertTrue([3] in self.game.battlefield['card_slot'].values)
        self.assertFalse([4] in self.game.battlefield['card_slot'].values)
        self.assertFalse([2] in self.game.hand['card_slot'].values)
        self.assertFalse([3] in self.game.hand['card_slot'].values)
        self.assertTrue([4] in self.game.hand['card_slot'].values)
        self.assertTrue(self.game.hand.index.is_monotonic_increasing)
        self.assertTrue(self.game.battlefield.index.is_monotonic_increasing)


if __name__ == '__main__':
    unittest.main()
