from data.deck_loader import load_deck_excel, write_deck
from mtg.deck import DeckMetrics, OpeningHandProbabilities, deck_reporter
from mtg.game import pick_card, island

# initialize decks either from Excel files or random gen dfs
deck_df1 = write_deck()
deck_df2 = load_deck_excel('rand_deck_1.xlsx')

# Initialize DeckMetrics and OpeningHandProbabilities instances for each deck
deck_metrics1 = DeckMetrics(deck_df1)
deck_metrics2 = DeckMetrics(deck_df2)
opening_hand_probs1 = OpeningHandProbabilities(deck_df1)
opening_hand_probs2 = OpeningHandProbabilities(deck_df2)

# Print deck stats and probabilities
print(deck_reporter(deck_metrics1, opening_hand_probs1))
print(deck_reporter(deck_metrics2, opening_hand_probs2))

# Pick cards for opening hands
opening_hand1 = pick_card(deck_metrics1.deck_library()['card_slot'], 7)
opening_hand2 = pick_card(deck_metrics2.deck_library()['card_slot'], 7)

# Print opening hands and land counts
print(f"deck1 opening hand: {opening_hand1}")
print(f"{island(deck_df1, opening_hand1)} Lands in deck1 opening hand")

print(f"deck2 opening hand: {opening_hand2}")
print(f"{island(deck_df2, opening_hand2)} Lands in deck2 opening hand")
