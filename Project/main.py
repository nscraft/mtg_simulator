import Project.Data.game_records
from Project.Data.deck_loader import DeckExcelMethod
from Project.Data.deck_gen import gen_rand_deck
from Project.Analytics.deck_opener import OpeningHandProbabilities
from Project.Analytics.deck_reporter import deck_reporter
from Project.Analytics.deck_metrics import DeckMetrics
from Project.Analytics.auto_game_reporter import game_report
from Project.MTG_elements.goldfish_handler import start_goldfish_game
from Project.MTG_elements.auto_game_handler import run_game


class MTGSim:
    def __init__(self):
        self.deck_name = None
        self.deck_df = None
        print("~~Welcome to MTG_Sim!~~")

    def select_deck(self):
        while True:
            print("1. Random")
            print("2. Load File")
            choice = input("Select method:")
            if choice == '1':
                self.deck_name = input("Enter deck name:")
                self.deck_df = gen_rand_deck()
                print(f"Deck {self.deck_name} loaded!")
                break
            if choice == '2':
                filename = input("Enter file name:")
                instance = DeckExcelMethod(filename)
                self.deck_name = instance.get_deck_name()
                self.deck_df = instance.load_deck_excel()
                if instance.error_msg == 1:
                    print(f"{filename} not found. Deck Not loaded.")
                else:
                    print(f"Deck {self.deck_name} loaded!")
                break
            else:
                print("Invalid method.")

    def print_report(self):
        if self.deck_df is not None:
            print(deck_reporter(
                deck_name=self.deck_name,
                deck_metrics=DeckMetrics(self.deck_df),
                opening_hand_probs=OpeningHandProbabilities(self.deck_df)))
        else:
            print("Please select a deck first.")

    def start_goldfishing(self):
        if self.deck_df is not None:
            start_goldfish_game(self.deck_df)
        else:
            print("Please select a deck first.")

    def start_auto_game(self):
        if self.deck_df is not None:
            run_game(self.deck_df)
            choice = input("Game finished.\nPrint save game records? (Y/N):")
            if choice == "Y":
                game_report()
            elif choice == 'N':
                pass
            else:
                print("Invalid choice.")
        else:
            print("Please select a deck first.")

    def main_loop(self):
        while True:
            print("\nMenu:")
            print("1. Select Deck")
            print("2. Print Report for Deck")
            print("3. Start Goldfish Game")
            print("4. Start Auto Game")
            print("5. Exit")
            choice = input("Enter your choice (1-5):")

            if choice == '1':
                self.select_deck()
            elif choice == '2':
                self.print_report()
            elif choice == '3':
                self.start_goldfishing()
            elif choice == '4':
                self.start_auto_game()
            elif choice == '5':
                Project.Data.game_records.destroy_files()
                print("Goodbye")
                break
            else:
                print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    mtg_sim = MTGSim()
    mtg_sim.main_loop()
