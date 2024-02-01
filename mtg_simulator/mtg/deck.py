from mtg.probability_engine import P_more_than_k, P_at_exactly_k


def deck_size(self):
    card_count = max(self.card_slot)
    return card_count


def deck_library(self):
    library_df = self[self.iscommander == 0]
    card_count = len(library_df)
    return card_count


def num_commander(self):
    commander_df = self[self.iscommander == 1]
    return len(commander_df)


def num_land(self):
    land_df = self[self.island == 1]
    return len(land_df)


def avg_mana_cost(self):
    nonland_df = self[self.island == 0]
    avg = nonland_df['mana_cost'].mean()
    round_avg = round(avg, 2)
    return round_avg


def num_ramp(self):
    ramp_df = self[self.isramp == 1]
    return len(ramp_df)


def avg_ramp_value(self):
    ramp_df = self[self.isramp == 1]
    avg = ramp_df['ramp_value'].mean()
    round_avg = round(avg, 2)
    return round_avg


def num_key(self):
    key_df = self[self.iskey == 1]
    return len(key_df)


def avg_key_value(self):
    key_df = self[self.iskey == 1]
    avg = key_df['ramp_value'].mean()
    round_avg = round(avg, 2)
    return round_avg


def zero_land_opener(self):
    cards_drawn = 7
    desired_lands = 0
    return P_at_exactly_k(N=deck_library(self), K=num_land(self), n=cards_drawn, k=desired_lands)


def four_land_opener(self):
    cards_drawn = 7
    min_lands = 4
    return P_more_than_k(N=deck_library(self), K=num_land(self), n=cards_drawn, k=min_lands)
