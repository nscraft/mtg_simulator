import unittest
import pandas as pd
import Project.Data.game_records


class TestWriteDeck(unittest.TestCase):

    def setUp(self):
        self.gs_df = pd.DataFrame({'column1': [1, 2, 3]})

    def test_update_records(self):
        Project.Data.game_records.update_gamestate_records(gamestate=self.gs_df)


if __name__ == '__main__':
    unittest.main()
