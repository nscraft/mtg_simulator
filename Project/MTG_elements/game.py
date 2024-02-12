import pandas as pd


class Game:
    def __init__(self, deck_df):
        self.library = deck_df[deck_df['iscommander'] == 0]
        self.hand = pd.DataFrame(columns=deck_df.columns)
        self.graveyard = pd.DataFrame(columns=deck_df.columns)
        self.turn = 1
        self.total_mana = 0
        self.play_land_for_turn()

    def shuffle(self):
        self.library = self.library.sample(frac=1).reset_index(drop=True)

    def draw_cards(self, num_cards):
        if num_cards > len(self.library):
            raise ValueError("Not enough cards in the library to draw.")
        drawn_cards = self.library.head(num_cards)
        self.library = self.library.iloc[num_cards:]
        self.hand = pd.concat([self.hand, drawn_cards], ignore_index=True)

    def play_land_for_turn(self):
        while self.turn <= 10:
            if self.turn == 1:
                self.draw_cards(7)
                print(f"Turn {self.turn} opener: {list(self.hand['card_slot'])}")
            else:
                self.draw_cards(1)
                print(f"Drew {list(self.hand['card_slot'])} as card for turn {self.turn}")

            # Check for land cards in hand
            lands_in_hand = self.hand[self.hand['island'] == 1]
            if not lands_in_hand.empty:
                # Assuming only one land played per turn
                land_to_play = lands_in_hand.iloc[0]
                self.graveyard = pd.concat([self.graveyard, pd.DataFrame([land_to_play])], ignore_index=True)
                self.hand = self.hand.drop(land_to_play.card_slot)
                self.total_mana += land_to_play['mana_value']

            print("Current graveyard:", list(self.graveyard['card_slot']))
            print("Total mana value in graveyard:", self.total_mana)

            self.turn += 1
