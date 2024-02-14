from Project.Data.deck_loader import DeckExcelMethod

filename = "deck_sample.xlsx"

deck_name = DeckExcelMethod(filename).get_deck_name()

print(f"Deck Name = {deck_name}")
