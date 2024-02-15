import pandas as pd


def game_report():
    records_hand = pd.read_csv("records_hand.csv")
    print(f"Hand Records:\n", records_hand)
