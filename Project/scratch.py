import pandas as pd

deck_df1 = pd.DataFrame({
    'card_slot': [1, 2, 3],
    'iscommander': [0, 0, 0],
    'island': [0, 1, 0],
    'mana_cost': [0, 0, 0],
    'isramp': [0, 0, 0],
    'mana_value': [0, 1, 0],
    'isdraw': [0, 0, 0],
    'draw_value': [0, 0, 0],
    'card_score': [0, 0, 0]
})


class Game:
    def __init__(self, deck_df):
        self.library = deck_df[deck_df['iscommander'] == 0]
        self.hand = deck_df
        self.battlefield = pd.DataFrame(columns=deck_df.columns)
        self.turn = 1
        self.total_mana = 0

    def play_land(self):
        lands_in_hand = self.hand[self.hand['island'] == 1]
        if not lands_in_hand.empty:
            land_to_play = lands_in_hand.iloc[0]
            self.battlefield = pd.concat([self.battlefield, pd.DataFrame([land_to_play])], ignore_index=True)
            self.hand = self.hand[self.hand['card_slot'] != land_to_play['card_slot']]
            self.total_mana += land_to_play['mana_value']
        print(f"library =\n {self.library}")
        print(f"hand =\n {self.hand}")
        print(f"battlefield =\n {self.battlefield}")


game_instance = Game(deck_df1)
game_instance.play_land()

# commit from work
