from data.deck_loader import load_deck_excel, write_deck, write_deck_withpartners
from mtg.deck import deck_size, num_lands
from mtg.probability_engine import P_more_than_k

# Cant run games at the moment, for now just returning deck stats and probabilities

# initialize decks either from Excel files or random gen dfs
deck_df1 = load_deck_excel('rand_deck_1.xlsx')
deck_df2 = load_deck_excel('rand_deck_2.xlsx')
deck_df3 = write_deck()
deck_df4 = write_deck_withpartners()


# on the first turn, what is my chance to draw 2 or more lands?
def two_land_opener(self):
    cards_drawn = 7
    desired_lands = 2
    return P_more_than_k(N=deck_size(self), K=num_lands(self), n=cards_drawn, k=desired_lands)


print(f"Deck 1 has a total of {num_lands(deck_df1)} lands.")
print(f"Deck 1 has a {round(two_land_opener(deck_df1) * 100, 2)}% chance of starting with 2 or more lands.")
print(f"Deck 2 has a total of {num_lands(deck_df2)} lands.")
print(f"Deck 2 has a {round(two_land_opener(deck_df2) * 100, 2)}% chance of starting with 2 or more lands.")
print(f"Deck 3 has a total of {num_lands(deck_df3)} lands.")
print(f"Deck 3 has a {round(two_land_opener(deck_df3) * 100, 2)}% chance of starting with 2 or more lands.")
print(f"Deck 4 has a total of {num_lands(deck_df4)} lands.")
print(f"Deck 4 has a {round(two_land_opener(deck_df4) * 100, 2)}% chance of starting with 2 or more lands.")
