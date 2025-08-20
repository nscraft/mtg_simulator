import pandas as pd
import Project.Analytics.probability_engine
import numpy as np
import math

class ProbabilityReport:
    MAX_TURNS = 12  # inclusive of turn 0 - 10

    def __init__(self, deck_metrics):
        self.deck_metrics = deck_metrics
        self.turn_number = 0
        self.deck_size = deck_metrics.deck_library_count()
        self.num_success_in_deck = deck_metrics.num_land()  # land card type based reporting
        self.cumulative_cards_drawn = 0
        self.hit_bonus_increment = deck_metrics.deck_distributed_draw_value()
        self.cumulative_hit_bonus = 0
        self.cumulative_successes_drawn = 0
        self.columns = [
            'Turn_number',
            'num_cards_in_deck_turn_start',
            'num_successes_in_deck_turn_start',
            'cards_drawn_this_turn',
            'cumulative_cards_drawn',
            'chance_of_drawing_0',
            'chance_of_drawing_exactly_k',
            'chance_of_drawing_at_most_k',
            'chance_of_drawing_more_than_k',
            'chance_of_drawing_at_least_k',
            'chance_of_drawing_less_than_k',
            'successes_drawn_this_turn',
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
            turn_start_deck_size = self.deck_size
            turn_start_num_successes = self.num_success_in_deck

            # cards_drawn_this_turn
            if self.turn_number == 0:
                # cards drawn turn 0 always 7
                cards_drawn_this_turn = 7
            else:
                # cards drawn each turn = base 1 + cumulative_hit_bonus (rounded down to whole card)
                cards_drawn_this_turn = 1 + math.floor(self.cumulative_hit_bonus)

            # after cumulative hit bonus is applied reset it
            if self.cumulative_hit_bonus >= 1:
                self.cumulative_hit_bonus = 0

            # Reset for the turn
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
                self.cumulative_hit_bonus += self.hit_bonus_increment
                if hit_result == 1:
                    self.num_success_in_deck -= 1
                    successes_drawn_this_turn += 1

            # Update cumulative trackers
            self.cumulative_successes_drawn += successes_drawn_this_turn

            # Record row
            new_row = {
                'Turn_number': [self.turn_number],
                'num_cards_in_deck_turn_start': [turn_start_deck_size],
                'num_successes_in_deck_turn_start': [turn_start_num_successes],
                'cards_drawn_this_turn': [cards_drawn_this_turn],
                'cumulative_cards_drawn': [self.cumulative_cards_drawn],
                'chance_of_drawing_0': [round(P_at_0, 2)],
                'chance_of_drawing_exactly_k': [round(P_at_exactly_k, 2)],
                'chance_of_drawing_at_most_k': [round(P_at_most_k, 2)],
                'chance_of_drawing_more_than_k': [round(P_more_than_k, 2)],
                'chance_of_drawing_at_least_k': [round(P_at_least_k, 2)],
                'chance_of_drawing_less_than_k': [round(P_less_than_k, 2)],
                'successes_drawn_this_turn': [successes_drawn_this_turn],
                'cumulative_successes_drawn': [self.cumulative_successes_drawn],
                'cumulative_success_as_percent_of_attempts': [
                    round(self.cumulative_successes_drawn / self.cumulative_cards_drawn if self.cumulative_cards_drawn > 0 else 0, 2)
                ]
            }
            self.dataframe = pd.concat([self.dataframe, pd.DataFrame(new_row)], ignore_index=True)
            # Update for next turn
            self.turn_number += 1

        self.dataframe = self.dataframe.sort_values(by='Turn_number').reset_index(drop=True)
        return self.dataframe
