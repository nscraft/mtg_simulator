import pandas as pd
import Project.Analytics.probability_engine
import numpy as np

def probability_report(pop_size, successes, sample_size, successes_in_sample, success_method) -> pd.DataFrame:
    """
    Generate a probability report based on hypergeometric distribution.
    Assumes 7 cards drawn on turn 0, and then 'sample_size' cards drawn on each subsequent turn.

    Args:
        pop_size (int): Total population size (N). AKA: Total number of cards in the deck.
        successes (int): Total number of successes in the population (K). AKA: Number of alike cards in the deck we want to draw.
        sample_size (int): Size of the sample drawn from the population (n). AKA: Cards drawn each turn.
        successes_in_sample (int): Number of alike cards we want to draw (k). AKA: Number of alike cards we want to draw each turn.
        success_method (str): Method to calculate success probabilities.
            Options are 'Law of Large Numbers' or 'at_least_k'.

    Returns:
        dataframe (pd.DataFrame): A DataFrame containing the probabilities for various conditions.
    """
    supported_methods = ['Law of Large Numbers', 'at_least_k']
    if success_method not in supported_methods:
        raise ValueError(f"Unsupported success method. Supported methods are: {supported_methods}")

    # constants
    MAX_TURNS = 12

    # variables updated each turn
    TURN_NUMBER = 0
    CARDS_DRAWN_TURN_0 = 7  # Number of cards drawn on turn 0
    CUMULATIVE_CARDS_DRAWN = 0
    DECK_SIZE = pop_size  # Total number of cards in the deck BEFORE draw
    NUM_SUCCESS_IN_DECK = successes  # Number of successes in the deck BEFORE draw
    CUMULATIVE_SUCCESSES_DRAWN = 0  # Cumulative successes drawn so far

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
    ]
    df = pd.DataFrame(columns=columns)

    # simulate remaining turns
    for turn in range(1, MAX_TURNS):
        # how many cards to draw this turn
        if turn == 1:
            cards_drawn = CARDS_DRAWN_TURN_0
        else:
            cards_drawn = sample_size

        # expected successes drawn BEFORE updating deck size
        if success_method == 'Law of Large Numbers':
            expected_successes_drawn_this_turn = int(cards_drawn * (NUM_SUCCESS_IN_DECK / DECK_SIZE))
        elif success_method == 'at_least_k':
            # calculate based on chance_of_drawing_at_least_k
            # example: if chance_of_drawing_at_least_k == 0.75, then assign a value 0 or 1 with a 75% chance of being 1, then multiply by cards_drawn
            expected_successes_drawn_this_turn = int(
                cards_drawn * np.random.binomial(1, Project.Analytics.probability_engine.P_at_least_k(DECK_SIZE, int(NUM_SUCCESS_IN_DECK), cards_drawn, successes_in_sample)))
        else:
            raise ValueError(f"Unsupported success method: {success_method}")

        # update cumulative trackers
        CUMULATIVE_CARDS_DRAWN += cards_drawn
        CUMULATIVE_SUCCESSES_DRAWN += expected_successes_drawn_this_turn

        # probabilities (decide whether you want per-turn or cumulative here)
        P_at_0 = Project.Analytics.probability_engine.P_at_0(DECK_SIZE, int(NUM_SUCCESS_IN_DECK), cards_drawn)
        P_at_exactly_k = Project.Analytics.probability_engine.P_at_exactly_k(DECK_SIZE, int(NUM_SUCCESS_IN_DECK),
                                                                             cards_drawn, successes_in_sample)
        P_at_most_k = Project.Analytics.probability_engine.P_at_most_k(DECK_SIZE, int(NUM_SUCCESS_IN_DECK), cards_drawn,
                                                                       successes_in_sample)
        P_more_than_k = Project.Analytics.probability_engine.P_more_than_k(DECK_SIZE, int(NUM_SUCCESS_IN_DECK),
                                                                           cards_drawn, successes_in_sample)
        P_at_least_k = Project.Analytics.probability_engine.P_at_least_k(DECK_SIZE, int(NUM_SUCCESS_IN_DECK),
                                                                         cards_drawn, successes_in_sample)
        P_less_than_k = Project.Analytics.probability_engine.P_less_than_k(DECK_SIZE, int(NUM_SUCCESS_IN_DECK),
                                                                           cards_drawn, successes_in_sample)

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
            'expected_successes_drawn_this_turn': [expected_successes_drawn_this_turn],
            'cumulative_expected_successes_drawn': [CUMULATIVE_SUCCESSES_DRAWN]
        })], ignore_index=True)

        # update for next turn
        TURN_NUMBER += 1
        DECK_SIZE -= cards_drawn
        NUM_SUCCESS_IN_DECK -= expected_successes_drawn_this_turn

    # Sort by Turn_number
    df = df.sort_values(by='Turn_number').reset_index(drop=True)
    return df

# call function
data = probability_report(99, 40, 2, 1, 'at_least_k')
# save data to csv
data.to_csv('probability_report.csv', index=False)