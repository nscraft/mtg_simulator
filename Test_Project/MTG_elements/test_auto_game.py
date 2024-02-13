import unittest
from your_game_module import Game  # Ensure this import matches your project structure
import pandas as pd


class TestGame(unittest.TestCase):
    def setUp(self):
        # Setup a mock deck dataframe
        self.mock_deck = pd.DataFrame({
            'card_slot': [1, 2, 3, 4, 5, 6],
            'iscommander': [1, 0, 0, 0, 0, 0],
            'island': [0, 0, 0, 1, 0, 1],
            'mana_cost': [2, 3, 1, 0, 4, 0],
            'mana_value': [0, 0, 0, 1, 0, 1]
        })
        self.game = Game(self.mock_deck)

    def test_initial_conditions(self):
        self.assertEqual(len(self.game.library), len(self.mock_deck) - self.mock_deck['iscommander'].sum())
        self.assertTrue(self.game.hand.empty)
        self.assertTrue(self.game.battlefield.empty)
        self.assertEqual(self.game.turn, 1)
        self.assertEqual(self.game.total_mana, 0)

    def test_draw_cards(self):
        self.game.draw_cards(1)
        self.assertEqual(len(self.game.hand), 1)
        self.assertEqual(len(self.game.library), len(self.mock_deck) - 1 - self.mock_deck['iscommander'].sum())

    def test_play_land(self):
        self.game.draw_cards(5)  # Assuming at least one land in the first 5 cards
        initial_battlefield_count = len(self.game.battlefield)
        self.game.play_land()
        self.assertEqual(len(self.game.battlefield), initial_battlefield_count + 1)
        self.assertTrue('Land' in self.game.battlefield['card_slot'].values)

    def test_cast_spells(self):
        self.game.total_mana = 5  # Assume player has 5 mana available
        self.game.draw_cards(3)  # Draw some non-land cards
        initial_hand_count = len(self.game.hand)
        self.game.cast_spells()
        # Check if at least one spell was cast
        self.assertTrue(len(self.game.hand) < initial_hand_count)
        self.assertTrue(len(self.game.battlefield) > 0)

    def test_play_turn(self):
        self.game.play_turn()  # Play first turn
        self.assertEqual(self.game.turn, 2)
        self.assertTrue(len(self.game.hand) > 0)
        self.assertTrue(len(self.game.library) < len(self.mock_deck))


if __name__ == '__main__':
    unittest.main()
