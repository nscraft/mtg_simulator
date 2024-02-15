import pandas as pd
import os


def reset_save():
    records_library = pd.DataFrame()
    records_library.to_csv("records_library.csv")
    records_hand = pd.DataFrame()
    records_hand.to_csv("records_hand.csv")
    records_battlefield = pd.DataFrame()
    records_battlefield.to_csv("records_battlefield.csv")


def update_records(game_library, game_hand, game_battlefield, game_turn):
    records_library = pd.read_csv("records_library.csv")
    game_library['turn'] = game_turn
    pd.concat([records_library, game_library], ignore_index=True).to_csv("records_library.csv")
    records_hand = pd.read_csv("records_hand.csv")
    game_hand['turn'] = game_turn
    pd.concat([records_hand, game_hand], ignore_index=True).to_csv("records_hand.csv")
    records_battlefield = pd.read_csv("records_battlefield.csv")
    game_battlefield['turn'] = game_turn
    pd.concat([records_battlefield, game_battlefield], ignore_index=True).to_csv("records_battlefield.csv")


def destroy_files():
    os.remove("records_library.csv")
    os.remove("records_hand.csv")
    os.remove("records_battlefield.csv")
