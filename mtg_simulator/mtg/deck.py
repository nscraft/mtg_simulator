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


def num_ramp_key(self):
    filter_df = self[
        (self.isramp == 1) & (self.iskey == 1)
        ]
    count = len(filter_df)
    return count


def num_other(self):
    other_df = self[
        (self.iscommander == 0) &
        (self.island == 0) &
        (self.isramp == 0) &
        (self.iskey == 0)
        ]
    other_count = len(other_df)
    return other_count


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
    avg = key_df['key_value'].mean()
    round_avg = round(avg, 2)
    return round_avg


def zero_land_opener(self):
    cards_drawn = 8
    desired_lands = 0
    probability = P_at_exactly_k(N=deck_library(self), K=num_land(self), n=cards_drawn, k=desired_lands)
    return probability


def four_land_opener(self):
    cards_drawn = 8
    min_lands = 4
    probability = P_more_than_k(N=deck_library(self), K=num_land(self), n=cards_drawn, k=min_lands)
    return probability

def twothree_land_opener(self):
    cards_drawn = 8
    probability = P_at_exactly_k(N=deck_library(self), K=num_land(self), n=cards_drawn, k=2) + P_at_exactly_k(N=deck_library(self), K=num_land(self), n=cards_drawn, k=3)
    return probability

def five_unplayable_opener(self):
    cards_drawn = 8
    filter_deck = self[
        (self['island'] == 0) & (self['mana_cost'] > 1)
        ]
    min_unplayable = 5
    probability = P_more_than_k(N=deck_library(self), K=len(filter_deck), n=cards_drawn, k=min_unplayable)
    return probability


def deck_reporter(deck):  # will need to add a deck name argument later
    report = (
        f"DECKNAME\n"
        f"Deck Stats:\n"
        f"{num_commander(deck)} commander(s) with {deck_library(deck)} cards in library.\n"
        f"Total of {num_land(deck)} lands.\n"
        f"Average mana cost of non-land cards is {avg_mana_cost(deck)}.\n"
        f"Total number of ramp cards is {num_ramp(deck)} and total number of key cards is {num_key(deck)}.\n"
        f"The average ramp value is {avg_ramp_value(deck)} and the average key value is {avg_key_value(deck)}.\n"
        f"There are {num_other(deck)} other (aka: "
        f"noncommander, nonland, nonramp, nonkey) cards.\n"
        f"Probabilities:\n"
        f"{round(twothree_land_opener(deck) * 100, 1)}% chance of drawing 2-3 land on turn 1?\n"
        f"{round(four_land_opener(deck) * 100, 1)}% chance of starting with 4 or more lands.\n"
        f"{round(zero_land_opener(deck) * 100, 1)}% chance of starting with zero land.\n"
        f"{round(five_unplayable_opener(deck) * 100, 1)}% chance of drawing 5 or more nonland cards that cost more than 1 mana on turn 1?\n"
        f"Probability of drawing playable ramp by turn 2?\n"
        f"Probability of drawing playable key card by turn 4?\n"
    )
    return report
