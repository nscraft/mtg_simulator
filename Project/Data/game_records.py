import pandas as pd
import os


def reset_save():
    records_library = pd.DataFrame()
    records_library.to_csv("records_library.csv", index=False)
    records_hand = pd.DataFrame()
    records_hand.to_csv("records_hand.csv", index=False)
    records_battlefield = pd.DataFrame()
    records_battlefield.to_csv("records_battlefield.csv", index=False)


def update_records(game_library, game_hand, game_battlefield, game_turn):
    try:
        records_library = pd.read_csv("records_library.csv")
    except pd.errors.EmptyDataError:
        records_library = pd.DataFrame()
    game_library['turn'] = game_turn
    pd.concat([records_library, game_library], ignore_index=True).to_csv("records_library.csv", index=False)
    try:
        records_hand = pd.read_csv("records_hand.csv")
    except pd.errors.EmptyDataError:
        records_hand = pd.DataFrame()
    game_hand['turn'] = game_turn
    pd.concat([records_hand, game_hand], ignore_index=True).to_csv("records_hand.csv", index=False)
    try:
        records_battlefield = pd.read_csv("records_battlefield.csv")
    except pd.errors.EmptyDataError:
        records_battlefield = pd.DataFrame()
    game_battlefield['turn'] = game_turn
    pd.concat([records_battlefield, game_battlefield], ignore_index=True).to_csv("records_battlefield.csv", index=False)


def destroy_files():
    os.remove("records_library.csv")
    os.remove("records_hand.csv")
    os.remove("records_battlefield.csv")
