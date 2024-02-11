import random


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
