import pandas as pd
import Project.Analytics.probability_engine
import numpy as np

class ProbabilityReport:
    MAX_TURNS = 12  # inclusive of turn 0 - 10

    def __init__(self, deck_metrics):
        self.deck_metrics = deck_metrics
        self.turn_number = 0
        self.deck_size = deck_metrics.deck_library_count()
        self.num_success_in_deck = deck_metrics.num_land()  # land card type based reporting
        self.cumulative_cards_drawn = 0
        self.cumulative_successes_drawn = 0
        self.cards_drawn_by_turn = {
            "turn_0": 7,  # Number of cards drawn on turn 0
            "turn_1": 1,
            "turn_2": 1,
            "turn_3": 1,
            "turn_4": 1,
            "turn_5": 1,
            "turn_6": 1,
            "turn_7": 1,
            "turn_8": 1,
            "turn_9": 1,
            "turn_10": 1,
        }
        self.columns = [
            'Turn_number',
            'num_cards_in_deck',
            'num_successes_in_deck',
            'cards_drawn',
            'cumulative_cards_drawn',
            'chance_of_drawing_0',
            'chance_of_drawing_exactly_k',
            'chance_of_drawing_at_most_k',
            'chance_of_drawing_more_than_k',
            'chance_of_drawing_at_least_k',
            'chance_of_drawing_less_than_k',
            'successes_drawn',
            'cumulative_successes_drawn',
            'cumulative_success_as_percent_of_attempts',
        ]
        self.dataframe = pd.DataFrame(columns=self.columns)

    def generate_report(self) -> pd.DataFrame:
        """
        Generate a probability report based on the deck metrics.

        Returns:
            pd.DataFrame: A DataFrame containing the probabilities for various conditions.
        """
        for turn in range(1, self.MAX_TURNS):
            cards_drawn_this_turn = self.cards_drawn_by_turn[f"turn_{self.turn_number}"]
            successes_drawn_this_turn = 0

            # Calculate total draw probabilities
            P_at_0 = Project.Analytics.probability_engine.P_at_0(self.deck_size, self.num_success_in_deck, cards_drawn_this_turn)
            P_at_exactly_k = Project.Analytics.probability_engine.P_at_exactly_k(self.deck_size, self.num_success_in_deck, cards_drawn_this_turn, 1)
            P_at_most_k = Project.Analytics.probability_engine.P_at_most_k(self.deck_size, self.num_success_in_deck, cards_drawn_this_turn, 1)
            P_more_than_k = Project.Analytics.probability_engine.P_more_than_k(self.deck_size, self.num_success_in_deck, cards_drawn_this_turn, 1)
            P_at_least_k = Project.Analytics.probability_engine.P_at_least_k(self.deck_size, self.num_success_in_deck, cards_drawn_this_turn, 1)
            P_less_than_k = Project.Analytics.probability_engine.P_less_than_k(self.deck_size, self.num_success_in_deck, cards_drawn_this_turn, 1)

            # Simulate drawing cards
            for _ in range(cards_drawn_this_turn):
                P_at_least_k = Project.Analytics.probability_engine.P_at_least_k(
                    self.deck_size, self.num_success_in_deck, 1, 1)
                hit_result = np.random.binomial(1, P_at_least_k)
                self.deck_size -= 1
                self.cumulative_cards_drawn += 1
                if hit_result == 1:
                    self.num_success_in_deck -= 1
                    successes_drawn_this_turn += 1

            # Update cumulative trackers
            self.cumulative_successes_drawn += successes_drawn_this_turn

            # Record row
            new_row = {
                'Turn_number': [self.turn_number],
                'num_cards_in_deck': [self.deck_size],
                'num_successes_in_deck': [self.num_success_in_deck],
                'cards_drawn': [cards_drawn_this_turn],
                'cumulative_cards_drawn': [self.cumulative_cards_drawn],
                'chance_of_drawing_0': [P_at_0],
                'chance_of_drawing_exactly_k': [P_at_exactly_k],
                'chance_of_drawing_at_most_k': [P_at_most_k],
                'chance_of_drawing_more_than_k': [P_more_than_k],
                'chance_of_drawing_at_least_k': [P_at_least_k],
                'chance_of_drawing_less_than_k': [P_less_than_k],
                'successes_drawn': [successes_drawn_this_turn],
                'cumulative_successes_drawn': [self.cumulative_successes_drawn],
                'cumulative_success_as_percent_of_attempts': [
                    self.cumulative_successes_drawn / self.cumulative_cards_drawn if self.cumulative_cards_drawn > 0 else 0
                ]
            }
            self.dataframe = pd.concat([self.dataframe, pd.DataFrame(new_row)], ignore_index=True)
            # Update for next turn
            self.turn_number += 1

        self.dataframe = self.dataframe.sort_values(by='Turn_number').reset_index(drop=True)
        return self.dataframe
