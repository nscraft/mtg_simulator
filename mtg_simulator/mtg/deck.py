
def deck_size(self):
    card_count = max(self.card_slot)
    return card_count


def num_lands(self):
    # card is land if 1, nonland if 0
    land_df = self[self.island == 1]
    return len(land_df)


def num_nonlands(self):
    # card is land if 1, nonland if 0
    land_df = self[self.island == 0]
    return len(land_df)
