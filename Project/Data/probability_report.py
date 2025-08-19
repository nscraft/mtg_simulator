import pandas as pd
import Project.Analytics.probability_engine
import numpy as np

def probability_report(deck_metrics) -> pd.DataFrame:
    """
    Generate a probability report based on the deck DataFrame.
    Begins from turn 0, max turn is 10.

    Args:
        deck_metrics (DeckMetrics): An instance of DeckMetrics containing the deck data.

    Returns:
        pd.DataFrame: A DataFrame containing the probabilities for various conditions.
        The dataframe contains the following fields:
            'Turn_number',
            'num_cards_in_deck_before_draw',
            'cards_drawn_this_turn',
            'num_successes_in_deck',
            'cumulative_cards_drawn',
            'chance_of_drawing_0',
            'chance_of_drawing_exactly_k',
            'chance_of_drawing_at_most_k',
            'chance_of_drawing_more_than_k',
            'chance_of_drawing_at_least_k',
            'chance_of_drawing_less_than_k'
            'expected_successes_drawn_this_turn',
            'cumulative_expected_successes_drawn'
            'cumulative_success_as_percent_of_attempts'
    """

    columns = [
        'Turn_number',
        'num_cards_in_deck_before_draw',
        'cards_drawn_this_turn',
        'num_successes_in_deck',
        'cumulative_cards_drawn',
        'chance_of_drawing_0',
        'chance_of_drawing_exactly_k',
        'chance_of_drawing_at_most_k',
        'chance_of_drawing_more_than_k',
        'chance_of_drawing_at_least_k',
        'chance_of_drawing_less_than_k'
        'expected_successes_drawn_this_turn',
        'cumulative_expected_successes_drawn'
        'cumulative_success_as_percent_of_attempts'  # cumulative_expected_successes_drawn / cumulative_cards_drawn
    ]
    df = pd.DataFrame(columns=columns)

    # constants
    MAX_TURNS = 12

    # variables updated each turn
    TURN_NUMBER = 0
    DECK_SIZE = deck_metrics.deck_library()  # Total number of cards in the deck BEFORE draw
    NUM_SUCCESS_IN_DECK = deck_metrics.num_land()  # Number of successes in the deck BEFORE draw
    CUMULATIVE_CARDS_DRAWN = 0
    CUMULATIVE_SUCCESSES_DRAWN = 0  # Cumulative successes drawn so far
    CARDS_DRAWN_BY_TURN = {
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

    for turn in range(1, MAX_TURNS):
        cards_drawn = CARDS_DRAWN_BY_TURN[f"turn_{TURN_NUMBER}"]
        successes_drawn_this_turn = 0

        # probabilities per turn
        P_at_0 = Project.Analytics.probability_engine.P_at_0(DECK_SIZE, NUM_SUCCESS_IN_DECK, cards_drawn)
        P_at_exactly_k = Project.Analytics.probability_engine.P_at_exactly_k(DECK_SIZE, NUM_SUCCESS_IN_DECK, cards_drawn, 1)
        P_at_most_k = Project.Analytics.probability_engine.P_at_most_k(DECK_SIZE, NUM_SUCCESS_IN_DECK, cards_drawn, 1)
        P_more_than_k = Project.Analytics.probability_engine.P_more_than_k(DECK_SIZE, NUM_SUCCESS_IN_DECK, cards_drawn, 1)
        P_at_least_k = Project.Analytics.probability_engine.P_at_least_k(DECK_SIZE, NUM_SUCCESS_IN_DECK, cards_drawn, 1)
        P_less_than_k = Project.Analytics.probability_engine.P_less_than_k(DECK_SIZE, NUM_SUCCESS_IN_DECK, cards_drawn, 1)

        # for each card drawn, determine success chance, return 1 or 0, and sum result.
        # example: if P_at_least_k == 0.75, then assign a value 0 or 1 with a 75% chance of being 1, iterate by cards_drawn
        for i in range(1, cards_drawn):
            DECK_SIZE -= cards_drawn
            hit = np.random.binomial(1,
                                     Project.Analytics.probability_engine.P_at_least_k(DECK_SIZE, NUM_SUCCESS_IN_DECK, 1, 1)
                                     )
            if hit == 1:
                NUM_SUCCESS_IN_DECK -= successes_drawn_this_turn
                successes_drawn_this_turn += 1

        # update cumulative trackers
        CUMULATIVE_SUCCESSES_DRAWN += successes_drawn_this_turn
        CUMULATIVE_CARDS_DRAWN += cards_drawn

        # record row
        df = pd.concat([df, pd.DataFrame({
            'Turn_number': [TURN_NUMBER],
            'num_cards_in_deck_before_draw': [DECK_SIZE],
            'num_successes_in_deck': [NUM_SUCCESS_IN_DECK],
            'cards_drawn_this_turn': [cards_drawn],
            'cumulative_cards_drawn': [CUMULATIVE_CARDS_DRAWN],
            'chance_of_drawing_0': [P_at_0],
            'chance_of_drawing_exactly_k': [P_at_exactly_k],
            'chance_of_drawing_at_most_k': [P_at_most_k],
            'chance_of_drawing_more_than_k': [P_more_than_k],
            'chance_of_drawing_at_least_k': [P_at_least_k],
            'chance_of_drawing_less_than_k': [P_less_than_k],
            'expected_successes_drawn_this_turn': [successes_drawn_this_turn],
            'cumulative_expected_successes_drawn': [CUMULATIVE_SUCCESSES_DRAWN],
            'cumulative_success_as_percent_of_attempts': [CUMULATIVE_SUCCESSES_DRAWN / CUMULATIVE_CARDS_DRAWN if CUMULATIVE_CARDS_DRAWN > 0 else 0]
        })], ignore_index=True)

        # update for next turn
        TURN_NUMBER += 1

    df = df.sort_values(by='Turn_number').reset_index(drop=True)
    return df