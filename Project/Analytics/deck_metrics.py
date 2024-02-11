class DeckMetrics:
    def __init__(self, deck):
        self.deck = deck

    def deck_size(self):
        return max(self.deck.card_slot)

    def deck_library(self):
        df = self.deck[self.deck['iscommander'] == 0]
        return df

    def deck_library_count(self):
        return len(self.deck[self.deck.iscommander == 0])

    def num_commander(self):
        return len(self.deck[self.deck.iscommander == 1])

    def num_land(self):
        return len(self.deck[self.deck.island == 1])

    def num_ramp(self):
        return len(self.deck[self.deck.isramp == 1])

    def num_key(self):
        return len(self.deck[self.deck.iskey == 1])

    def num_rampkey(self):
        return len(self.deck[(self.deck.isramp == 1) & (self.deck.iskey == 1)])

    def num_other(self):
        other_df = self.deck[
            (self.deck.iscommander == 0) &
            (self.deck.island == 0) &
            (self.deck.isramp == 0) &
            (self.deck.iskey == 0)
            ]
        other_count = len(other_df)
        return other_count

    def avg_mana_cost(self):
        avg = self.deck[self.deck.island == 0]['mana_cost'].mean()
        round_avg = round(avg, 2)
        return round_avg

    def avg_ramp_value(self):
        ramp_df = self.deck[self.deck.isramp == 1]
        avg = ramp_df['ramp_value'].mean()
        round_avg = round(avg, 2)
        return round_avg

    def avg_key_value(self):
        key_df = self.deck[self.deck.iskey == 1]
        avg = key_df['key_value'].mean()
        round_avg = round(avg, 2)
        return round_avg
