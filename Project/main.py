from Project.Data.deck_loader import DeckExcelMethod, write_deck
from Project.Analytics.deck_metrics import DeckMetrics
from Project.Analytics.deck_opener import OpeningHandProbabilities
from Project.Analytics.deck_reporter import deck_reporter
from Project.MTG_elements.goldfish_handler import start_goldfish_game

# initialize decks either from Excel files or random gen dfs
deck1_name = "Programed RandDeck"
deck1_df = write_deck()
deck2 = DeckExcelMethod('deck_sample.xlsx')
deck2_name = DeckExcelMethod.deck_name(deck2)
deck2_df = DeckExcelMethod.load_deck_excel(deck2)

# Initialize DeckMetrics and OpeningHandProbabilities instances for each deck
deck_metrics1 = DeckMetrics(deck1_df)
opening_hand_probs1 = OpeningHandProbabilities(deck1_df)


def print_menu():
    print("\nMenu:")
    print("1. Print deck report for deck 1")
    print("2. Start Goldfish Game")
    print("3. Exit")


def main():
    while True:
        print_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            print(deck_reporter(deck1_name, deck_metrics1, opening_hand_probs1))
        elif choice == '2':
            start_goldfish_game(deck1_df)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    main()
