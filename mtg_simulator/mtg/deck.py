from data.deck_loader import load_deck_excel, write_deck, write_deck_withpartners
from mtg.probability_engine import P_more_than_k

# initialize decks either from Excel files or random gen dfs
deck_df1 = write_deck()
deck_df2 = write_deck_withpartners()
deck_excel1 = load_deck_excel('rand_deck_1.xlsx')


def deck_size(self):
    card_count = max(self.card_slot)
    return card_count


def num_lands(self):
    # card is land if 1, nonland if 0
    land_df = self[self.island == 1]
    return len(land_df)


def num_nonlands(self):
    # card is land if 1, nonland if 0
    land_df = self[self.island == 0]
    return len(land_df)


# on the first turn, what is my chance to draw 2 or more lands?
def two_land_opener(self):
    cards_drawn = 7
    desired_lands = 2
    return P_more_than_k(N=deck_size(self), K=num_lands(self), n=cards_drawn, k=desired_lands)


print(f"Deck 1 has a total of {num_lands(deck_df1)} lands.")
print(f"Deck 1 has a {round(two_land_opener(deck_df1) * 100, 2)}% chance of starting with 2 or more lands.")
print(f"Deck 2 has a total of {num_lands(deck_df2)} lands.")
print(f"Deck 2 has a {round(two_land_opener(deck_df2) * 100, 2)}% chance of starting with 2 or more lands.")
print(f"Deck 3 has a total of {num_lands(deck_excel1)} lands.")
print(f"Deck 3 has a {round(two_land_opener(deck_excel1) * 100, 2)}% chance of starting with 2 or more lands.")
