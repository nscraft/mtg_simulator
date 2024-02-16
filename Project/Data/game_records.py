import os

import pandas as pd

records_library_accumulator = pd.DataFrame()
records_hand_accumulator = pd.DataFrame()
records_battlefield_accumulator = pd.DataFrame()


def reset_records_inMemory():
    global records_library_accumulator, records_hand_accumulator, records_battlefield_accumulator
    records_library_accumulator = pd.DataFrame()
    records_hand_accumulator = pd.DataFrame()
    records_battlefield_accumulator = pd.DataFrame()


def update_records(game_library, game_hand, game_battlefield, game_turn, game_num):
    global records_library_accumulator, records_hand_accumulator, records_battlefield_accumulator

    game_library['turn'] = game_turn
    game_library['game'] = game_num
    game_hand['turn'] = game_turn
    game_hand['game'] = game_num
    game_battlefield['turn'] = game_turn
    game_battlefield['game'] = game_num
    records_library_accumulator = pd.concat([records_library_accumulator, game_library], ignore_index=True)
    records_hand_accumulator = pd.concat([records_hand_accumulator, game_hand], ignore_index=True)
    records_battlefield_accumulator = pd.concat([records_battlefield_accumulator, game_battlefield], ignore_index=True)


def finalize_records():
    global records_library_accumulator, records_hand_accumulator, records_battlefield_accumulator

    records_library_accumulator.to_csv("records_library.csv", index=False)
    records_hand_accumulator.to_csv("records_hand.csv", index=False)
    records_battlefield_accumulator.to_csv("records_battlefield.csv", index=False)


def destroy_files():
    try:
        os.remove("records_library.csv")
    except FileNotFoundError:
        pass
    try:
        os.remove("records_hand.csv")
    except FileNotFoundError:
        pass
    try:
        os.remove("records_battlefield.csv")
    except FileNotFoundError:
        pass
