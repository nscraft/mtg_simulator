from data.deck_loader import load_deck_excel, write_deck, write_deck_withpartners
from mtg.deck import num_commander, deck_library, num_land, avg_mana_cost, num_ramp, avg_ramp_value, deck_size, num_key, \
    avg_key_value, four_land_opener, zero_land_opener

# initialize decks either from Excel files or random gen dfs
deck_df1 = write_deck()
deck_df2 = write_deck_withpartners()
deck_excel1 = load_deck_excel('rand_deck_1.xlsx')

# Cant run games at the moment, for now just returning deck stats and probabilities


def deck_reporter(deck):  # will need to add a deck name argument later
    report = (
        f"Deck Stats: ~deckname~\n"
        f"{num_commander(deck)} commander(s) with {deck_library(deck)} cards in library.\n"
        f"Total of {num_land(deck)} lands.\n"
        f"Average mana cost of non-land cards is {avg_mana_cost(deck)}.\n"
        f"Total number of ramp cards is {num_ramp(deck)} and total number of key cards is {num_key(deck)}.\n"
        f"The average ramp value is {avg_ramp_value(deck)} and the average key value is {avg_key_value(deck)}.\n"
        f"There are {deck_size(deck)-(num_land(deck)+num_ramp(deck)+num_key(deck)+num_commander(deck))} other (aka: "
        f"noncommander, nonland, nonramp, nonkey) cards.\n"
        f"Probabilities: ~deckname~\n"
        f"Probability of drawing 2-3 land on turn 1?\n"
        f"{round(four_land_opener(deck) * 100, 1)}% chance of starting with 4 or more lands.\n"
        f"{round(zero_land_opener(deck) * 100, 1)}% chance of starting with zero land.\n"
        f"Probability of drawing 5 or more unplayable cards on turn 1?\n"
        f"Probability of drawing 5 or more unplayable cards by turn 3?\n"
        f"Probability of drawing playable ramp by turn 2?\n"
        f"Probability of drawing playable key card by turn 4?\n"
    )
    return report


print(deck_reporter(deck_df1))
