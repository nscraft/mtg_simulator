from Project.Data.deck_loader import DeckExcelMethod, gen_deck
from Project.MTG_elements.game import Game

# initialize decks either from Excel files or random gen dfs
deck1_name = "Programed RandDeck"
deck1_df = gen_deck()

# Run a game
game_instance = Game(deck1_df)
