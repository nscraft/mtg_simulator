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
