from Project.Analytics.deck_metrics import DeckMetrics
from Project.Data.deck_loader import DeckExcelMethod, gen_deck
from Project.Analytics.deck_opener import OpeningHandProbabilities
from Project.Analytics.deck_reporter import deck_reporter
from Project.MTG_elements.goldfish_handler import start_goldfish_game


class MTGSim:
    def __init__(self):
        self.deck_name = None
        self.deck_df = None
        print("~~Welcome to MTG_Sim!~~")

    def select_deck(self):
        while True:
            choice = input("Select method: (rand/load_file).")

            if choice == 'rand':
                self.deck_name = input("Enter deck name:")
                self.deck_df = gen_deck()
                print(f"Deck {self.deck_name} loaded!")
                break
            if choice == 'load_file':
                filename = input("Enter file name including extension:")
                DeckExcelMethod(filename)
                self.deck_name = DeckExcelMethod.deck_name
                self.deck_df = DeckExcelMethod.load_deck_excel
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

    def main_loop(self):
        while True:
            print("\nMenu:")
            print("1. Select Deck")
            print("2. Print Report for Deck")
            print("3. Start Goldfish Game")
            print("4. Exit")
            choice = input("Enter your choice (1-4):")

            if choice == '1':
                self.select_deck()
            elif choice == '2':
                self.print_report()
            elif choice == '3':
                self.start_goldfishing()
            elif choice == '4':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    mtg_sim = MTGSim()
    mtg_sim.main_loop()
