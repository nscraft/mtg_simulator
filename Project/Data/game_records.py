import pandas as pd

library_records = pd.DataFrame()
hand_records = pd.DataFrame()
battlefield_records = pd.DataFrame()


def reset_save():
    library_records.drop(library_records.index, inplace=True)
    hand_records.drop(hand_records.index, inplace=True)
    battlefield_records.drop(battlefield_records.index, inplace=True)


def update_records(game_library, game_hand, game_battlefield, game_turn):
    game_library['turn'] = game_turn
    pd.concat([library_records, game_library], ignore_index=True)
    game_hand['turn'] = game_turn
    pd.concat([hand_records, game_hand], ignore_index=True)
    game_battlefield['turn'] = game_turn
    pd.concat([battlefield_records, game_battlefield], ignore_index=True)
