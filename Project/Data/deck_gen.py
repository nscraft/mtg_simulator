import pandas as pd
import numpy as np
import os


def gen_rand_deck():
    deck_list = pd.DataFrame({'card_slot': range(1, 101)})
    deck_list['iscommander'] = np.where(deck_list['card_slot'] == 1, 1, 0)
    deck_list['island'] = np.where(deck_list['iscommander'] == 1, 0, np.random.randint(0, 2, size=len(deck_list)))
    deck_list['mana_cost'] = np.where(deck_list['island'] == 1, 0, np.random.randint(1, 8, size=len(deck_list)))
    deck_list['isramp'] = np.where(deck_list['island'] == 1, 0, np.random.randint(0, 2, size=len(deck_list)))
    deck_list['mana_value'] = np.where(
        deck_list['island'] == 1, 1,
        np.where(deck_list['isramp'] == 1, np.random.randint(1, 5, size=len(deck_list)), 0)
    )
    deck_list['isdraw'] = np.where(deck_list['island'] == 1, 0, np.random.randint(0, 2, size=len(deck_list)))
    deck_list['draw_value'] = np.where(deck_list['isdraw'] == 0, 0, np.random.randint(1, 8, size=len(deck_list)))
    deck_list['card_score'] = np.where(
        (deck_list['island'] == 1) | (deck_list['isramp'] == 1) | (deck_list['isdraw'] == 1), 0,
        deck_list['mana_cost'])
    return deck_list
