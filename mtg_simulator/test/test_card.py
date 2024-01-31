import unittest
from mtg import deck, main


class TestDeck(unittest.TestCase):

    def deck_size_is_100(self):
        assert deck.Deck.deck_size(main.deck_list_1) == 100
