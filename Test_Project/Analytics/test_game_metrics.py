import unittest
import pandas as pd

from Project.Analytics.game_metrics import GameMetrics


class TestDeck(unittest.TestCase):

    def setUp(self):
        lib = pd.DataFrame(
            {
                'card_slot': [],
                'iscommander': [],
                'island': [],
                'mana_cost': [],
                'isramp': [],
                'mana_value': [],
                'isdraw': [],
                'draw_value': [],
                'card_score': [],
                'game': [],
                'turn': []
            })

        hand = pd.DataFrame(
            {
                'card_slot': [],
                'iscommander': [],
                'island': [],
                'mana_cost': [],
                'isramp': [],
                'mana_value': [],
                'isdraw': [],
                'draw_value': [],
                'card_score': [],
                'game': [],
                'turn': []
            })
        bf = pd.DataFrame(
            {
                'card_slot': [],
                'iscommander': [],
                'island': [],
                'mana_cost': [],
                'isramp': [],
                'mana_value': [],
                'isdraw': [],
                'draw_value': [],
                'card_score': [],
                'game': [],
                'turn': []
            })
        self.instance = GameMetrics(lib, hand, bf)

    def test_final_score(self):
        result = self.instance.final_score()
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
