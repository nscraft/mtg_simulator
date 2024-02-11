import pandas as pd
import random


class Game:
    def __init__(self, deck_df):
        self.library = list(deck_df[deck_df['iscommander'] == 0]['card_slot'])
        self.hand = deck_df[deck_df['iscommander'] == 1]
        self.graveyard = pd.DataFrame()
        self.turn = 1
        self.total_mana = 0
        self.play_land_for_turn()

    def draw_cards(self, num_cards):
        if num_cards > len(self.library):
            raise ValueError("Not enough cards in the library to draw.")
        drawn_cards = random.sample(population=self.library, k=num_cards)
        self.library = [card for card in self.library if card not in drawn_cards]
        self.hand.update(drawn_cards)
        return drawn_cards

    def play_land_for_turn(self):
        while self.turn <= 10:
            if self.turn == 1:
                self.draw_cards(7)
            else:
                self.draw_cards(1)
            print(f"Drawn cards on turn {self.turn}:", self.hand)

            # Check for land cards in hand
            lands_in_hand = self.hand[self.hand['island'] == 1]
            if not lands_in_hand.empty:
                # Assuming only one land played per turn
                land_to_play = lands_in_hand.iloc[0]
                self.graveyard = pd.concat([self.graveyard, pd.DataFrame([land_to_play])], ignore_index=True)
                self.hand = self.hand.drop(land_to_play.card_slot)
                self.total_mana += land_to_play['mana_value']

            print("Current graveyard:", self.graveyard)
            print("Total mana value in graveyard:", self.total_mana)

            self.turn += 1
