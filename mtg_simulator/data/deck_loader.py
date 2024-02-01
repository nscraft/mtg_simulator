import pandas as pd
import numpy as np
import os


def load_deck_excel(deck_name):
    current_dir = os.path.dirname(__file__)
    excel_file_path = os.path.join(current_dir, deck_name)
    return pd.read_excel(excel_file_path)


def write_deck():
    deck_list = pd.DataFrame({'card_slot': range(1, 101)})
    deck_list["iscommander"] = np.where(deck_list['card_slot'] == 1, 1, 0)
    deck_list['island'] = np.where(deck_list['iscommander'] == 1, 0, np.random.randint(0, 2, size=len(deck_list)))
    deck_list['mana_cost'] = np.where(deck_list['island'] == 1, 0, np.random.randint(0, 8, size=len(deck_list)))
    deck_list['isramp'] = np.where(deck_list['island'] == 1, 0, np.random.randint(0, 2, size=len(deck_list)))
    deck_list['ramp_value'] = np.where(deck_list['isramp'] == 0, 0, np.random.randint(1, 5, size=len(deck_list)))
    deck_list['iskey'] = np.where(deck_list['island'] == 1, 0, np.random.randint(0, 2, size=len(deck_list)))
    deck_list['key_value'] = np.where(deck_list['iskey'] == 0, 0, np.random.randint(1, 8, size=len(deck_list)))
    return deck_list


def write_deck_withpartners():
    deck_list = pd.DataFrame({'card_slot': range(1, 101)})
    deck_list["iscommander"] = np.where(deck_list['card_slot'].isin([1, 2]), 1, 0)
    deck_list['island'] = np.where(deck_list['iscommander'] == 1, 0, np.random.randint(0, 2, size=len(deck_list)))
    deck_list['mana_cost'] = np.where(deck_list['island'] == 1, 0, np.random.randint(0, 8, size=len(deck_list)))
    deck_list['isramp'] = np.where(deck_list['island'] == 1, 0, np.random.randint(0, 2, size=len(deck_list)))
    deck_list['ramp_value'] = np.where(deck_list['isramp'] == 0, 0, np.random.randint(1, 5, size=len(deck_list)))
    deck_list['iskey'] = np.where(deck_list['island'] == 1, 0, np.random.randint(0, 2, size=len(deck_list)))
    deck_list['key_value'] = np.where(deck_list['iskey'] == 0, 0, np.random.randint(1, 8, size=len(deck_list)))
    return deck_list


# BE VERY CAREFUL WHEN OVERWRITING SOURCE FILES
deck_df1 = write_deck()
deck_df2 = write_deck()
deck_df1.to_excel('rand_deck_1.xlsx')
deck_df2.to_excel('rand_deck_2.xlsx')
