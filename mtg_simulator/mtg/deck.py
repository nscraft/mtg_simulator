import pandas as pd

deck_df1 = pd.read_excel('C:/Users/nick.craft/PycharmProjects/mtg_simulator/rand_deck_1.xlsx')
deck_df2 = pd.read_excel('C:/Users/nick.craft/PycharmProjects/mtg_simulator/rand_deck_2.xlsx')


def deck_size(self):
    return len(self)


def num_lands(self):
    # card is land if 1, nonland if 0
    land_df = self[self.island == 1]
    return len(land_df)


def num_nonlands(self):
    # card is land if 1, nonland if 0
    land_df = self[self.island == 0]
    return len(land_df)
