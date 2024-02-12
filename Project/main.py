from Project.Data.deck_loader import DeckExcelMethod, write_deck
from Project.Analytics.deck_metrics import DeckMetrics
from Project.Analytics.deck_opener import OpeningHandProbabilities
from Project.Analytics.deck_reporter import deck_reporter
from Project.MTG_elements.goldfish import GoldfishGame

# initialize decks either from Excel files or random gen dfs
deck1_name = "Programed RandDeck"
deck1_df = write_deck()
deck2 = DeckExcelMethod('deck_sample.xlsx')
deck2_name = DeckExcelMethod.deck_name(deck2)
deck2_df = DeckExcelMethod.load_deck_excel(deck2)

# Initialize DeckMetrics and OpeningHandProbabilities instances for each deck
deck_metrics1 = DeckMetrics(deck1_df)
opening_hand_probs1 = OpeningHandProbabilities(deck1_df)

# Print deck stats and probabilities
print(deck_reporter(deck1_name, deck_metrics1, opening_hand_probs1))


# Run a goldfish game
game = GoldfishGame(deck1_df)
print("\nSTART GAME: GOLDFISH")
goldfish_open = game.draw_cards(num_cards=7)  # Draw 7 card opener
print(f"Opening hand: {game.hand}")
print(f"Cards in Library: {len(game.library)}")
print(f"Cards in Graveyard: {len(game.graveyard)}")
game.discard_hand()
print("Hand discarded.")
print(f"Updated hand: {game.hand}")
print(f"Cards in Updated Library: {len(game.library)}")
print(f"Cards in Updated Graveyard: {len(game.graveyard)}")
try:
    goldfish_draw_more = int(input("How many more cards would you like to draw?"))
except ValueError:
    print("Please enter a valid integer.")
    goldfish_draw_more = 0
print(f"{goldfish_draw_more} more cards drawn.")
additional_cards_drawn = game.draw_cards(goldfish_draw_more)
print(f"Updated hand: {game.hand}")
print(f"Cards in Updated Library: {len(game.library)}")
print(f"Cards in Updated Graveyard: {len(game.graveyard)}")
