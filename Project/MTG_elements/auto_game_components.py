import pandas as pd


class GameComponents:
    def __init__(self, deck_df):
        self.library = deck_df[deck_df['iscommander'] == 0]
        self.hand = pd.DataFrame(columns=deck_df.columns)
        self.battlefield = pd.DataFrame(columns=deck_df.columns)
        self.total_mana = 0

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
        spells_in_hand = self.hand[self.hand['island'] == 0].copy()
        spells_to_play = pd.DataFrame()
        mana_for_turn = self.total_mana
        spells_in_hand.sort_values(by='mana_cost', inplace=True)
        for index, card in spells_in_hand.iterrows():
            if card['mana_cost'] <= mana_for_turn:
                card_df = pd.DataFrame([card])
                spells_to_play = pd.concat([spells_to_play, card_df], ignore_index=True)
                mana_for_turn -= card['mana_cost']
                self.hand = self.hand.drop(index)
                self.draw_cards(spells_to_play['draw_value'].sum())
            else:
                break

        self.battlefield = pd.concat([self.battlefield, spells_to_play]).reset_index(drop=True)
        self.hand = self.hand.reset_index(drop=True)
