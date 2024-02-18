import Project.Data.game_records
import Project.Data.deck_loader
import Project.Data.deck_gen
import Project.Analytics.deck_opener
import Project.Analytics.deck_metrics
import Project.Analytics.deck_reporter
import Project.Analytics.game_reporter_improved
import Project.Events.goldfish_handler
import Project.Events.game_handler_improved


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
                self.deck_df = Project.Data.deck_gen.gen_rand_deck()
                print(f"Deck {self.deck_name} loaded!")
                break
            if choice == '2':
                filename = input("Enter file name:")
                instance = Project.Data.deck_loader.DeckExcelMethod(filename)
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
            print(Project.Analytics.deck_reporter.deck_reporter(
                deck_name=self.deck_name,
                deck_metrics=Project.Analytics.deck_metrics.DeckMetrics(self.deck_df),
                opening_hand_probs=Project.Analytics.deck_opener.OpeningHandProbabilities(self.deck_df)))
        else:
            print("Please select a deck first.")

    def start_goldfishing(self):
        if self.deck_df is not None:
            Project.Events.goldfish_handler.start_goldfish(self.deck_df)
        else:
            print("Please select a deck first.")

    def start_game(self):
        if self.deck_df is not None:
            print("Running game...")
            Project.Events.game_handler_improved.run_game(self.deck_df, 1)
            choice = input("Game finished.\nPrint game records? (Y/N):")
            if choice == "Y":
                Project.Analytics.game_reporter_improved.game_report()
            elif choice == 'N':
                pass
            else:
                print("Invalid choice.")
        else:
            print("Please select a deck first.")

    def start_100_games(self):
        if self.deck_df is not None:
            print("Running games...")
            Project.Events.game_handler_improved.run_game(self.deck_df, 100)
            choice = input("Games finished.\nPrint game records? (Y/N):")
            if choice == "Y":
                Project.Analytics.game_reporter_improved.game_report_multi()
            elif choice == "N":
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
            print("3. Start Goldfishing")
            print("4. Run a Game")
            print("5. Run 100 Games")
            print("6. Exit")
            choice = input("Enter your choice (1-6):")

            if choice == '1':
                self.select_deck()
            elif choice == '2':
                self.print_report()
            elif choice == '3':
                self.start_goldfishing()
            elif choice == '4':
                self.start_game()
            elif choice == '5':
                self.start_100_games()
            elif choice == '6':
                Project.Data.game_records.destroy_files()
                print("Goodbye")
                break
            else:
                print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    mtg_sim = MTGSim()
    mtg_sim.main_loop()
