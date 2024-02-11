from Project.Analytics.probability_engine import P_more_than_k, P_at_exactly_k
from Project.Analytics.deck_metrics import DeckMetrics


class OpeningHandProbabilities:
    cards_drawn = 7

    def __init__(self, deck):
        self.deck = deck
        self.deck_metrics = DeckMetrics(deck)

    def zero_land_opener(self):
        hits = 0
        probability = P_at_exactly_k(N=self.deck_metrics.deck_library_count(), K=self.deck_metrics.num_land(),
                                     n=self.cards_drawn, k=hits)
        return probability

    def fourormore_land_opener(self):
        hits = 4
        probability = P_more_than_k(N=self.deck_metrics.deck_library_count(), K=self.deck_metrics.num_land(),
                                    n=self.cards_drawn, k=hits)
        return probability

    def twothree_land_opener(self):
        minhit = 2
        maxhit = 3
        minprobability = P_at_exactly_k(N=self.deck_metrics.deck_library_count(), K=self.deck_metrics.num_land(),
                                        n=self.cards_drawn, k=minhit)
        maxprobability = P_at_exactly_k(N=self.deck_metrics.deck_library_count(), K=self.deck_metrics.num_land(),
                                        n=self.cards_drawn, k=maxhit)
        return minprobability + maxprobability

    def five_unplayable_opener(self):
        filter_deck = self.deck[
            (self.deck['island'] == 0) & (self.deck['mana_cost'] > 1)
            ]
        min_unplayable = 5
        probability = P_more_than_k(N=self.deck_metrics.deck_library_count(), K=len(filter_deck), n=self.cards_drawn,
                                    k=min_unplayable)
        return probability
