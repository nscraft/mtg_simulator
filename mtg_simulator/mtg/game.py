# here we will define how turns work and how games are won.
# games are dependent on players and decks
# when called by main.py, a winner will be returned
# main.py can call multiple games inorder to simulate a tournament
import random


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
