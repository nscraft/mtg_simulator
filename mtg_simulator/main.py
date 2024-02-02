from data.deck_loader import DeckExcelMethod, write_deck
from mtg.deck import DeckMetrics, OpeningHandProbabilities, deck_reporter
from mtg.game import pick_card, island

# initialize decks either from Excel files or random gen dfs
deck1_name = "Programed RandDeck"
deck1_df = write_deck()
deck2 = DeckExcelMethod('rand_deck_1.xlsx')
deck2_name = DeckExcelMethod.deck_name(deck2)
deck2_df = DeckExcelMethod.load_deck_excel(deck2)



# Initialize DeckMetrics and OpeningHandProbabilities instances for each deck
deck_metrics1 = DeckMetrics(deck1_df)
deck_metrics2 = DeckMetrics(deck2_df)
opening_hand_probs1 = OpeningHandProbabilities(deck1_df)
opening_hand_probs2 = OpeningHandProbabilities(deck1_df)

# Print deck stats and probabilities
print(deck_reporter(deck1_name, deck_metrics1, opening_hand_probs1))
print(deck_reporter(deck2_name, deck_metrics2, opening_hand_probs2))

# Pick cards for opening hands
opening_hand1 = pick_card(deck_metrics1.deck_library()['card_slot'], 7)
opening_hand2 = pick_card(deck_metrics2.deck_library()['card_slot'], 7)

# Print opening hands and land counts
print(f"{deck1_name} opening hand: {opening_hand1}")
print(f"{island(deck1_df, opening_hand1)} Lands in deck1 opening hand")

print(f"{deck2_name} opening hand: {opening_hand2}")
print(f"{island(deck2_df, opening_hand2)} Lands in deck2 opening hand")
