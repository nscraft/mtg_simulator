class GameMetrics:
    def __init__(self, game_data):
        self.records = game_data
        self.final_bf = self.records[
            (self.records['turn'] == self.records['turn'].max()) & (self.records['zone'] == 'battlefield')]
        self.final_hand = self.records[
            (self.records['turn'] == self.records['turn'].max()) & (self.records['zone'] == 'hand')]

    def max_games(self):
        return self.records['game'].max()

    def max_turn(self):
        return self.records['turn'].max()

    def final_score(self):
        game_scores = self.final_bf.groupby('game')['card_score'].sum()
        return game_scores.mean()

    def final_lands_inplay(self):
        final_lands = self.final_bf[self.final_bf['island'] == 1].groupby('game')['card_slot'].count()
        return final_lands.mean()

    def final_mana_available(self):
        mana_value = self.final_bf.groupby('game')['mana_value'].sum()
        return mana_value.mean()

    def final_card_count_battlefield(self):
        cards = self.final_bf.groupby('game').size()
        return cards.mean()

    def final_card_count_hand(self):
        cards = self.final_hand.groupby('game').size()
        return cards.mean()
