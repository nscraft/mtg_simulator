import unittest
import pandas as pd
from Project.Events.game import GameComponents


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
        self.game.set_deck_to_library()
        self.game.draw_cards(5)
        initial_hand_count = len(self.game.table[self.game.table['zone'] == 'hand'])
        self.assertEqual(5, initial_hand_count)
        self.game.play_land()
        self.game.cast_spells()
        updated_hand = len(self.game.table[self.game.table['zone'] == 'hand'])
        self.assertTrue(updated_hand < initial_hand_count)


if __name__ == '__main__':
    unittest.main()
