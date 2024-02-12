from Project.Data.deck_loader import DeckExcelMethod, write_deck
from Project.MTG_elements.game import Game


deck1_name = "Programed RandDeck"
deck1_df = write_deck()

print(f"deck data frame = \n {deck1_df}\n")

select_row = deck1_df.iloc[3]

select_df = deck1_df[deck1_df['card_slot'] == select_row]
print(f"selected df =\n {select_df}\n")

filter_df = deck1_df.drop(select_df.index)

print(f"filter df = \n{filter_df}")
