import pandas as pd


class SaveGame:
    def __init__(self):
        self.library_records = pd.DataFrame()
        self.hand_records = pd.DataFrame()
        self.battlefield_records = pd.DataFrame()

    def save_state(self, library_df, hand_df, battlefield_df, turn):
        library_df['turn'] = turn
        self.library_records = pd.concat([self.library_records, library_df], ignore_index=True)
        hand_df['turn'] = turn
        self.hand_records = pd.concat([self.hand_records, hand_df], ignore_index=True)
        battlefield_df['turn'] = turn
        self.battlefield_records = pd.concat([self.battlefield_records, battlefield_df], ignore_index=True)
