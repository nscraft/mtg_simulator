import unittest
from mtg.game import pick_card


class TestDeck(unittest.TestCase):

    def setUp(self):
        self.pool = [1, 2, 3, 4]
        self.cards = 2

    def test_pick_card(self):
        result = pick_card(self.pool, self.cards)
        count = len(result)
        self.assertIsNotNone(result)
        self.assertEqual(count, self.cards)
        self.assertTrue(all(card in self.pool for card in result))


if __name__ == '__main__':
    unittest.main()
