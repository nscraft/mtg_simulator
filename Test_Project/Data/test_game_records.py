import unittest
import pandas as pd
from Project.Data.game_records import update_records, reset_records_inMemory, destroy_files


class TestWriteDeck(unittest.TestCase):

    def setUp(self):
        self.lib_df = pd.DataFrame({'column1': [1, 2, 3]})
        self.ha_df = pd.DataFrame({'column1': [1, 2, 3]})
        self.bf_df = pd.DataFrame({'column1': [1, 2, 3]})

    def test_update_records(self):
        update_records(game_library=self.lib_df, game_hand=self.ha_df, game_battlefield=self.bf_df, game_turn=1, game_num=1)
        update_records(game_library=self.lib_df, game_hand=self.ha_df, game_battlefield=self.bf_df, game_turn=2, game_num=1)


if __name__ == '__main__':
    unittest.main()
