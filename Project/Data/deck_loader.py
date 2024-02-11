import pandas as pd
import numpy as np
import os


class DeckExcelMethod:
    def __init__(self, file_name):
        self.deck_name = file_name

    def deck_name(self):
        return str(self.deck_name)

    def load_deck_excel(self):
        current_dir = os.path.dirname(__file__)
        excel_file_path = os.path.join(current_dir, self.deck_name)
        return pd.read_excel(excel_file_path)


def write_deck():
    deck_list = pd.DataFrame({'card_slot': range(1, 101)})
    deck_list['iscommander'] = np.where(deck_list['card_slot'] == 1, 1, 0)
    deck_list['island'] = np.where(deck_list['iscommander'] == 1, 0, np.random.randint(0, 2, size=len(deck_list)))
    deck_list['mana_cost'] = np.where(deck_list['island'] == 1, 0, np.random.randint(0, 8, size=len(deck_list)))
    deck_list['isramp'] = np.where(deck_list['island'] == 1, 0, np.random.randint(0, 2, size=len(deck_list)))
    deck_list['ramp_value'] = np.where(deck_list['isramp'] == 0, 0, np.random.randint(1, 5, size=len(deck_list)))
    deck_list['isdraw'] = np.where(deck_list['island'] == 1, 0, np.random.randint(0, 2, size=len(deck_list)))
    deck_list['draw_value'] = np.where(deck_list['isdraw'] == 0, 0, np.random.randint(1, 8, size=len(deck_list)))
    deck_list['card_score'] = np.where(
        (deck_list['island'] == 1) | (deck_list['isramp'] == 1) | (deck_list['isdraw'] == 1), 0,
        deck_list['mana_cost'])
    return deck_list
