from mtg.probability_engine import P_more_than_k, P_at_exactly_k


class DeckMetrics:
    def __init__(self, deck):
        self.deck = deck

    def deck_size(self):
        return max(self.deck.card_slot)

    def deck_library(self):
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


class OpeningHandProbabilities:
    cards_drawn = 7

    def __init__(self, deck):
        self.deck = deck
        self.deck_metrics = DeckMetrics(deck)

    def zero_land_opener(self):
        hits = 0
        probability = P_at_exactly_k(N=self.deck_metrics.deck_library(), K=self.deck_metrics.num_land(),
                                     n=self.cards_drawn, k=hits)
        return probability

    def fourormore_land_opener(self):
        hits = 4
        probability = P_more_than_k(N=self.deck_metrics.deck_library(), K=self.deck_metrics.num_land(),
                                    n=self.cards_drawn, k=hits)
        return probability

    def twothree_land_opener(self):
        minhit = 2
        maxhit = 3
        minprobability = P_at_exactly_k(N=self.deck_metrics.deck_library(), K=self.deck_metrics.num_land(),
                                     n=self.cards_drawn, k=minhit)
        maxprobability = P_at_exactly_k(N=self.deck_metrics.deck_library(), K=self.deck_metrics.num_land(),
                                        n=self.cards_drawn, k=maxhit)
        return minprobability + maxprobability

    def five_unplayable_opener(self):
        filter_deck = self.deck[
            (self.deck['island'] == 0) & (self.deck['mana_cost'] > 1)
            ]
        min_unplayable = 5
        probability = P_more_than_k(N=self.deck_metrics.deck_library(), K=len(filter_deck), n=self.cards_drawn,
                                    k=min_unplayable)
        return probability


def deck_reporter(deck_metrics, opening_hand_probs):  # will need to add a deck name argument later
    report = (
        f"DECKNAME\n"
        f"Deck Stats:\n"
        f"{deck_metrics.num_commander()} commander(s) with {deck_metrics.deck_library()} cards in library.\n"
        f"Total of {deck_metrics.num_land()} lands.\n"
        f"Average mana cost of non-land cards is {deck_metrics.avg_mana_cost()}.\n"
        f"Total number of ramp cards is {deck_metrics.num_ramp()} and total number of key cards is {deck_metrics.num_key()}.\n"
        f"The average ramp value is {deck_metrics.avg_ramp_value()} and the average key value is {deck_metrics.avg_key_value()}.\n"
        f"There are {deck_metrics.num_other()} other (aka: "
        f"noncommander, nonland, nonramp, nonkey) cards.\n"
        f"Probabilities:\n"
        f"{round(opening_hand_probs.twothree_land_opener() * 100, 1)}% chance of drawing 2-3 land on turn 1?\n"
        f"{round(opening_hand_probs.fourormore_land_opener() * 100, 1)}% chance of starting with 4 or more lands.\n"
        f"{round(opening_hand_probs.zero_land_opener() * 100, 1)}% chance of starting with zero land.\n"
        f"{round(opening_hand_probs.five_unplayable_opener() * 100, 1)}% chance of drawing 5 or more nonland cards "
        f"that cost more than 1 mana on turn 1?\n"
        f"Probability of drawing playable ramp by turn 2?\n"
        f"Probability of drawing playable key card by turn 4?\n"
    )
    return report
