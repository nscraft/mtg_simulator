class GameMetrics:
    def __init__(self, library_df, hand_df, battlefield_df):
        self.library = library_df
        self.hand = hand_df
        self.battlefield = battlefield_df

    def max_turn(self):
        return self.battlefield["turn"].max()

    def final_score(self):
        final_bf = self.battlefield[self.battlefield["turn"] == self.max_turn()]
        return final_bf["card_score"].sum()

    def final_lands_inplay(self):
        final_bf = self.battlefield[self.battlefield["turn"] == self.max_turn()]
        return len(final_bf["island"] == 1)

    def final_mana_value(self):
        final_bf = self.battlefield[self.battlefield["turn"] == self.max_turn()]
        return final_bf["mana_value"].sum()

    def final_card_count_battlefield(self):
        final_bf = self.battlefield[self.battlefield["turn"] == self.max_turn()]
        return len(final_bf)

    def final_card_count_hand(self):
        final_hand = self.hand[self.hand["turn"] == self.max_turn()]
        return len(final_hand)
