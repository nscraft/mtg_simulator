class GameMetrics:
    def __init__(self, library_df, hand_df, battlefield_df):
        self.library = library_df
        self.hand = hand_df
        self.battlefield = battlefield_df

    def max_turn(self):
        return self.battlefield["turn"].max()

    def final_score(self):
        return self.battlefield["card_score"][self.battlefield["turn"] == self.max_turn()].sum()

    def final_lands_inplay(self):
        return len(self.battlefield[self.battlefield["island"] == 1][self.battlefield["turn"] == self.max_turn()])

    def final_mana_value(self):
        return self.battlefield["mana_value"][self.battlefield["turn"] == self.max_turn()].sum()

    def final_card_count_battlefield(self):
        final_bf = self.battlefield[self.battlefield["turn"] == self.max_turn()]
        return len(final_bf)

    def final_card_count_hand(self):
        final_hand = self.hand[self.hand["turn"] == self.max_turn()]
        return len(final_hand)
