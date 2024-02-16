import unittest
from Project.MTG_elements.game_handler import run_game, run_game_multiple
import pandas as pd


class TestGame(unittest.TestCase):
    def setUp(self):
        self.mock_deck = pd.DataFrame({
            'card_slot': [1, 2, 3, 4, 5, 6],
            'iscommander': [1, 0, 0, 0, 0, 0],
            'island': [0, 0, 0, 1, 0, 1],
            'mana_cost': [2, 3, 1, 0, 4, 0],
            'mana_value': [0, 0, 0, 1, 0, 1]
        })
        self.game_num = 3

    def test_run_game(self):
        result = run_game(self.mock_deck, self.game_num)
        return result

    def test_game_multiple(self):
        result = run_game_multiple(self.mock_deck, self.game_num)
        return result


if __name__ == '__main__':
    unittest.main()
