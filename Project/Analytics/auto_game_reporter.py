import pandas as pd

from Project.Analytics.auto_game_metrics import GameMetrics


def game_report():
    instance = GameMetrics(
        library_df=pd.read_csv("records_library.csv"),
        hand_df=pd.read_csv("records_hand.csv"),
        battlefield_df=pd.read_csv("records_battlefield.csv")
    )
    print(f"{instance.max_turn()} total turns were recorded.")
    print(f"--Final turn stats--")
    print("Total card score:", instance.final_score())
    print("Total cards in play:", instance.final_card_count_battlefield())
    print("Lands in play:", instance.final_lands_inplay())
    print("Total Mana available:", instance.final_mana_value())
    print("Cards still in hand:", instance.final_card_count_hand())
