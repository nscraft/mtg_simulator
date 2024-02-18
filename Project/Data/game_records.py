import os
import pandas as pd

gamestate_accumulator = pd.DataFrame(columns=
                                     ['card_slot', 'iscommander', 'island', 'mana_cost', 'isramp', 'mana_value',
                                      'isdraw', 'draw_value', 'card_score', 'zone', 'game', 'turn'])


def reset_gamestate_inMemory():
    global gamestate_accumulator
    gamestate_accumulator = pd.DataFrame(columns=
                                         ['card_slot', 'iscommander', 'island', 'mana_cost', 'isramp', 'mana_value',
                                          'isdraw', 'draw_value', 'card_score', 'zone', 'game', 'turn'])


def update_gamestate_records(gamestate):
    global gamestate_accumulator
    gamestate_accumulator = pd.concat([gamestate_accumulator, gamestate], ignore_index=True)


def save_records():
    global gamestate_accumulator
    gamestate_accumulator.to_csv("save_game_records.csv", index=False)


def destroy_files():
    try:
        os.remove("save_game_records.csv")
    except FileNotFoundError:
        pass
