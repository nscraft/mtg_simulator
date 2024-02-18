import unittest
import pandas as pd

from Project.Analytics.game_metrics import GameMetrics


class TestDeck(unittest.TestCase):

    def setUp(self):
        gamestate = pd.DataFrame(
            {
                'card_slot': [1, 2, 3, 4] * 4,
                'iscommander': [0] * 16,
                'island': [0] * 16,
                'mana_cost': [0] * 16,
                'isramp': [0] * 16,
                'mana_value': [0] * 16,
                'isdraw': [0] * 16,
                'draw_value': [0] * 16,
                'card_score': [0] * 16,
                'zone': ['battlefield'] * 16,
                'game': [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2],
                'turn': [1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2]
            })
        self.instance = GameMetrics(game_data=gamestate)

    def test_final_score(self):
        result = self.instance.final_score()
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
