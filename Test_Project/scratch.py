import pandas as pd

from Project.Data.deck_loader import DeckExcelMethod

filename = "deck_sample"

deck_name = DeckExcelMethod(filename).get_deck_name()

print(f"Deck Name = {deck_name}")
deck_df = DeckExcelMethod(filename).load_deck_excel()
print(deck_df)
deck_df_forced = pd.read_excel("C:/Users/nick.craft/PycharmProjects/mtg_simulator/Project/Data/deck_sample.xlsx")
print(deck_df_forced)
