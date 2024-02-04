from data.deck_loader import DeckExcelMethod, write_deck
from mtg.deck import DeckMetrics, OpeningHandProbabilities, deck_reporter
from mtg.game import pick_card, island, GoldfishGame

# initialize decks either from Excel files or random gen dfs
deck1_name = "Programed RandDeck"
deck1_df = write_deck()
deck2 = DeckExcelMethod('deck_sample.xlsx')
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

# Use pick_card method
opening_hand1 = pick_card(deck_metrics1.deck_library()['card_slot'], 7)
print(f"{deck1_name} opening hand: {opening_hand1}")
print(f"{island(deck1_df, opening_hand1)} Lands in deck1 opening hand")

# Run a goldfish game
game = GoldfishGame(deck1_df)
print("\nSTART GAME: GOLDFISH")
goldfish_open = game.draw_cards(num_cards=7)  # Draw 7 card opener
print(f"Opening hand: {game.hand}")
print(f"Cards in Library: {len(game.library)}")
print(f"Cards in Graveyard: {len(game.graveyard)}")
game.discard_hand()
print("Hnad discarded.")
print(f"Updated hand: {game.hand}")
print(f"Cards in Updated Library: {len(game.library)}")
print(f"Cards in Updated Graveyard: {len(game.graveyard)}")
goldfish_draw_more = 7
print("7 more cards drawn.")
additional_cards_drawn = game.draw_cards(goldfish_draw_more)
print(f"Updated hand: {game.hand}")
print(f"Cards in Updated Library: {len(game.library)}")
print(f"Cards in Updated Graveyard: {len(game.graveyard)}")
