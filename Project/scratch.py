from Project.Data.deck_loader import DeckExcelMethod, write_deck
from Project.MTG_elements.game import Game

# initialize decks either from Excel files or random gen dfs
deck1_name = "Programed RandDeck"
deck1_df = write_deck()

print(f"deck data frame {deck1_df}")

deck_tolist = list(deck1_df['card_slot'])

print(f"list {deck_tolist}")
