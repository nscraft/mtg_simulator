# here we will define how turns work and how games are won.
# games are dependent on players and decks
# when called by main.py, a winner will be returned
# main.py can call multiple games inorder to simulate a tournament
import random
import pandas as pd


# this class is deprecated
class UniqueRandomGenerator:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.generated = set()

    def generate_unique(self):
        if len(self.generated) == (self.end - self.start + 1):
            raise Exception("All possible numbers have been generated.")

        while True:
            number = random.randint(self.start, self.end)
            if number not in self.generated:
                self.generated.add(number)
                return number


def pick_card(card_pool, num_card):
    if isinstance(card_pool, pd.Series):
        card_pool = card_pool.tolist()
    if num_card > len(card_pool):
        raise ValueError("Number of cards to pick exceeds the available cards in the pool.")
    picked_cards = set()
    while len(picked_cards) < num_card:
        card = random.choice(card_pool)
        picked_cards.add(card)
    return picked_cards


def island(deck, cards):
    lands_inDeck = deck[deck['island'] == 1]
    island_inHand = lands_inDeck['card_slot'].isin(cards)
    land_count = island_inHand.sum()
    return land_count


class GoldfishGame:
    def __init__(self, deck_df):
        self.library = list(deck_df['card_slot'])
        self.hand = set()
        self.graveyard = set()

    def draw_cards(self, num_cards):
        if num_cards > len(self.library):
            raise ValueError("Not enough cards in the library to draw.")
        drawn_cards = random.sample(population=self.library, k=num_cards)
        self.library = [card for card in self.library if card not in drawn_cards]
        self.hand.update(drawn_cards)
        return drawn_cards

    def discard_cards(self, cards_to_discard):
        if not cards_to_discard.issubset(self.hand):
            raise ValueError("Cannot discard cards that are not in hand.")
        self.hand -= cards_to_discard
        self.graveyard.update(cards_to_discard)

    def discard_hand(self):
        self.graveyard.update(self.hand)
        self.hand.clear()
