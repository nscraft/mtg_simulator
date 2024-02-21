class GameComponents:
    def __init__(self, deck_df):
        self.table = deck_df
        self.table['zone'] = 'NA'
        self.table['game'] = 0
        self.table['turn'] = 0
        self.bonus_draw = 0

    def set_commander_to_command_zone(self):
        self.table.loc[self.table['iscommander'] == 1, 'zone'] = 'command'

    def set_deck_to_library(self):
        self.table.loc[self.table['iscommander'] == 0, 'zone'] = 'library'

    def shuffle(self):
        library_rows = self.table[self.table['zone'] == 'library']
        shuffled_library_rows = library_rows.sample(frac=1).reset_index(drop=True)
        library_indices = library_rows.index
        self.table.loc[library_indices, :] = shuffled_library_rows.values

    def draw_cards(self, draw_num):
        library_indices = self.table[self.table['zone'] == 'library'].index[:draw_num]
        if not library_indices.empty:
            self.table.loc[library_indices, 'zone'] = 'hand'
        else:
            pass

    def play_land(self):
        lands_in_hand = self.table[(self.table['zone'] == 'hand') & (self.table['island'] == 1)]
        if not lands_in_hand.empty:
            land_to_play = lands_in_hand.iloc[0].name
            self.table.loc[land_to_play, 'zone'] = 'battlefield'
        else:
            pass

    def cast_spells(self):
        mana_for_turn = self.table[self.table['zone'] == 'battlefield'].mana_value.sum()
        spells_in_hand = self.table[
            (self.table['zone'] == 'hand') & (self.table['island'] == 0)].sort_values(by='mana_cost', ascending=False)
        spells_to_play_indices = []
        self.bonus_draw = 0
        if not spells_in_hand.empty:
            for index, card in spells_in_hand.iterrows():
                if card['mana_cost'] <= mana_for_turn or mana_for_turn == 0 and card['mana_cost'] == 0:
                    mana_for_turn -= card['mana_cost']
                    spells_to_play_indices.append(index)
                    self.bonus_draw += card['draw_value']
        if spells_to_play_indices:
            self.table.loc[spells_to_play_indices, 'zone'] = 'battlefield'
