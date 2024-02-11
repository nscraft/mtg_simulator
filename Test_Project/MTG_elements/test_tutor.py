import unittest
import pandas as pd
from Project.MTG_elements.tutor import pick_card


class TestCardPicker(unittest.TestCase):

    def setUp(self):
        self.pool = [1, 2, 3, 4]
        self.cards = 2

    def test_pick_card_returns_correct_number_of_cards(self):
        result = pick_card(self.pool, self.cards)
        count = len(result)
        self.assertIsNotNone(result)
        self.assertEqual(count, self.cards)
        self.assertTrue(all(card in self.pool for card in result))
