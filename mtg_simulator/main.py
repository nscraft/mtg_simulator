from data.deck_loader import load_deck_excel, write_deck
from mtg.deck import deck_reporter

# initialize decks either from Excel files or random gen dfs
deck_df1 = write_deck()
deck_df2 = load_deck_excel('rand_deck_1.xlsx')

# Cant run games at the moment, for now just returning deck stats and probabilities

print(deck_reporter(deck_df1))
print(deck_reporter(deck_df2))
