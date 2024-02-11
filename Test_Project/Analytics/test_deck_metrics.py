import unittest
import pandas as pd
from Project.Analytics.deck_metrics import DeckMetrics


class TestDeck(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_deck = pd.DataFrame(
            {'card_slot': [1, 2, 3, 4, 100],
             'iscommander': [1, 0, 0, 0, 0],
             'island': [0, 1, 1, 0, 0],
             'isramp': [0, 0, 0, 1, 0],
             'ramp_value': [0, 0, 0, 2, 0],
             'iskey': [1, 0, 0, 0, 1],
             'key_value': [1, 1, 0, 0, 7],
             'mana_cost': [3, 0, 0, 1, 3]
             })

    def test_deck_length(self):
        deck_metrics_instance = DeckMetrics(self.test_deck)
        result = deck_metrics_instance.deck_size()
        self.assertEqual(result, 100, "deck size test failed")

    def test_deck_library(self):
        deck_metrics_instance = DeckMetrics(self.test_deck)
        result = deck_metrics_instance.deck_library()
        self.assertEqual(len(result), 4, "deck size failed")

    def test_num_land(self):
        deck_metrics_instance = DeckMetrics(self.test_deck)
        result = deck_metrics_instance.num_land()
        self.assertEqual(result, 2, "land count test failed")

    def test_avg_mana_cost(self):
        deck_metrics_instance = DeckMetrics(self.test_deck)
        result = deck_metrics_instance.avg_mana_cost()
        self.assertEqual(result, 2.33)

    def test_num_other(self):
        deck_metrics_instance = DeckMetrics(self.test_deck)
        result = deck_metrics_instance.num_other()
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
