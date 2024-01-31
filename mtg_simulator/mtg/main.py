from deck import deck_df1, deck_df2, deck_size, num_lands
from probability_engine import P_more_than_k

# Cant run games at the moment, for now just returning deck stats and probabilities

# on the first turn, what is my chance to draw 2 or more lands?
def two_land_opener(deck):
    cards_drawn = 7
    desired_lands = 2
    return P_more_than_k(N=deck_size(deck), K=num_lands(deck), n=cards_drawn, k=desired_lands)


print(f"Deck 1 has a total of {num_lands(deck_df1)} lands.")
print(f"Deck 1 has a {round(two_land_opener(deck_df1) * 100, 2)}% chance of starting with 2 or more lands.")
print(f"Deck 2 has a total of {num_lands(deck_df2)} lands.")
print(f"Deck 2 has a {round(two_land_opener(deck_df2) * 100, 2)}% chance of starting with 2 or more lands.")
