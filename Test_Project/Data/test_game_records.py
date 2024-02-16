import pandas as pd
from Project.Data.game_records import update_records, reset_records_inMemory, destroy_files

lib_df = pd.DataFrame({'column1': [1, 2, 3]})
ha_df = pd.DataFrame({'column1': [1, 2, 3]})
bf_df = pd.DataFrame({'column1': [1, 2, 3]})
turn = 2

update_records(game_library=lib_df, game_hand=ha_df, game_battlefield=bf_df, game_turn=1)
update_records(game_library=lib_df, game_hand=ha_df, game_battlefield=bf_df, game_turn=2)

print(pd.read_csv("records_library.csv"))
