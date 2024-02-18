import pandas as pd
import Project.Analytics.game_metrics_improved


def game_report():
    data = pd.read_csv("save_game_records.csv")
    instance = Project.Analytics.game_metrics_improved.GameMetrics(game_data=data)
    print(f"{instance.max_turn()} total turns were recorded.")
    print(f"--Summary Stats--")
    print("Total card score:", instance.final_score())
    print("Total cards in play:", instance.final_card_count_battlefield())
    print("Lands in play:", instance.final_lands_inplay())
    print("Total Mana available:", instance.final_mana_available())
    print("Cards still in hand:", instance.final_card_count_hand())


def game_report_multi():
    data = pd.read_csv("save_game_records.csv")
    instance = Project.Analytics.game_metrics_improved.GameMetrics(game_data=data)
    print(f"Total games played:", instance.max_games())
    print("--Summary Stats--")
    print("Average score:", instance.final_score())
