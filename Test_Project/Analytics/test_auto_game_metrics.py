import unittest
import pandas as pd
from Project.Analytics.auto_game_metrics import GameMetrics


class TestDeck(unittest.TestCase):

    def setUp(self):
        lib = pd.read_csv("records_library.csv")
        hand = pd.read_csv("records_hand.csv")
        bf = pd.read_csv("records_battlefield.csv")
        self.instance = GameMetrics(lib, hand, bf)

    def test_max_turn(self):
        result = self.instance.max_turn()
        self.assertEqual(result, 10)

    def test_final_score(self):
        result = self.instance.final_score()
        self.assertTrue(result > 1)


if __name__ == '__main__':
    unittest.main()
