import pandas as pd


class Game:
    def __init__(self, deck_df):
        self.library = deck_df[deck_df['iscommander'] == 0]
        self.hand = pd.DataFrame(columns=deck_df.columns)
        self.battlefield = pd.DataFrame(columns=deck_df.columns)
        self.turn = 1
        self.total_mana = 0
        self.play_turn()

    def shuffle(self):
        self.library = self.library.sample(frac=1).reset_index(drop=True)

    def draw_cards(self, num_cards):
        if num_cards > len(self.library):
            raise ValueError("Not enough cards in the library to draw.")
        drawn_cards = self.library.head(num_cards)
        self.library = self.library.iloc[num_cards:]
        self.hand = pd.concat([self.hand, drawn_cards], ignore_index=True)

    def play_land(self):
        lands_in_hand = self.hand[self.hand['island'] == 1]
        if not lands_in_hand.empty:
            land_to_play = lands_in_hand.iloc[0]
            self.battlefield = pd.concat([self.battlefield, pd.DataFrame([land_to_play])], ignore_index=True)
            self.hand = self.hand[self.hand['card_slot'] != land_to_play['card_slot']]
            self.total_mana += land_to_play['mana_value']

    def cast_spells(self):
        spells_to_play = pd.DataFrame()
        mana_for_turn = self.total_mana
        self.hand.sort_values(by='mana_cost', inplace=True)
        for index, card in self.hand.iterrows():
            if card['mana_cost'] <= self.total_mana:
                card_df = pd.DataFrame([card])
                spells_to_play = pd.concat([spells_to_play, card_df], ignore_index=True)
                mana_for_turn -= card['mana_cost']
                self.hand = self.hand.drop(index)
            else:
                break
        self.battlefield = pd.concat([self.battlefield, spells_to_play]).reset_index(drop=True)
        self.hand.reset_index(drop=True)

    def play_turn(self):
        while self.turn <= 10:
            if self.turn == 1:
                self.shuffle()
                self.draw_cards(7)
                print(f"Turn {self.turn} opener: {list(self.hand['card_slot'])}")
            else:
                self.draw_cards(1)
                print(f"Turn:", self.turn)
                print(f"Cards in hand:", list(self.hand['card_slot']))

            print("playing lands...")
            self.play_land()
            print("Cards in play:", list(self.battlefield['card_slot']))
            print("Total mana value in play:", self.total_mana)
            print("Cards in Library:", len(self.library))
            print("casting spells...")
            self.cast_spells()
            print("Cards in play:", list(self.battlefield['card_slot']))

            self.turn += 1
