import pandas as pd
import os


class DeckExcelMethod:
    def __init__(self, file_name):
        self.deck_name = file_name
        self.error_msg = 0

    def get_deck_name(self):
        return str(self.deck_name)

    def load_deck_excel(self):
        current_dir = os.path.dirname(__file__)
        excel_file_path = os.path.join(current_dir, self.deck_name)
        if not os.path.exists(excel_file_path):
            self.error_msg = 1
        else:
            pd.read_excel(excel_file_path)
