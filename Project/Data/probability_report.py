import pandas as pd
import Project.Analytics.probability_engine

def probability_report(pop_size, successes, sample_size, successes_in_sample) -> pd.DataFrame:
    """
    Generate a probability report based on hypergeometric distribution.
    Assumes 7 cards drawn on turn 0, and then 'sample_size' cards drawn on each subsequent turn.
    Updates the number of cards in the deck and successes in the deck after each turn.
    Remaining successes updated based on expected successes drawn (law of large numbers).

    Args:
        pop_size (int): Total population size (N).
        successes (int): Total number of successes in the population (K).
        sample_size (int): Size of the sample drawn from the population (n).
        successes_in_sample (int): Number of alike cards we want to draw (k).

    Returns:
        dataframe (pd.DataFrame): A DataFrame containing the probabilities for various conditions.
    """
    # variables updated each turn
    TURN_NUMBER = 0
    CARDS_DRAWN = 7
    DECK_SIZE = pop_size  # Total number of cards in the deck BEFORE draw
    NUM_SUCCESS_IN_DECK = successes  # Number of successes in the deck BEFORE draw

    columns = [
        'Turn_number',
        'num_cards_in_deck_before_draw',
        'num_successes_in_deck',
        'cards_drawn',
        'chance_of_drawing_0',
        'chance_of_drawing_exactly_k',
        'chance_of_drawing_at_most_k',
        'chance_of_drawing_more_than_k',
        'chance_of_drawing_at_least_k',
        'chance_of_drawing_less_than_k'
    ]
    df = pd.DataFrame(columns=columns)
    max_turns = 10

    # simulate remaining turns
    for turn in range(1, max_turns):
        # Calculate probabilities
        P_at_0 = Project.Analytics.probability_engine.P_at_0(DECK_SIZE, NUM_SUCCESS_IN_DECK, CARDS_DRAWN)
        P_at_exactly_k = Project.Analytics.probability_engine.P_at_exactly_k(DECK_SIZE, NUM_SUCCESS_IN_DECK, CARDS_DRAWN, successes_in_sample)
        P_at_most_k = Project.Analytics.probability_engine.P_at_most_k(DECK_SIZE, NUM_SUCCESS_IN_DECK, CARDS_DRAWN, successes_in_sample)
        P_more_than_k = Project.Analytics.probability_engine.P_more_than_k(DECK_SIZE, NUM_SUCCESS_IN_DECK, CARDS_DRAWN, successes_in_sample)
        P_at_least_k = Project.Analytics.probability_engine.P_at_least_k(DECK_SIZE, NUM_SUCCESS_IN_DECK, CARDS_DRAWN, successes_in_sample)
        P_less_than_k = Project.Analytics.probability_engine.P_less_than_k(DECK_SIZE, NUM_SUCCESS_IN_DECK, CARDS_DRAWN, successes_in_sample)

        # modify CARDS_DRAWN after first turn
        if turn > 1:
            CARDS_DRAWN = sample_size

        # Append to DataFrame
        df = pd.concat(
            [df, pd.DataFrame({
                'Turn_number': [TURN_NUMBER],
                'num_cards_in_deck_before_draw': [DECK_SIZE],
                'num_successes_in_deck': [NUM_SUCCESS_IN_DECK],
                'cards_drawn': [CARDS_DRAWN],
                'chance_of_drawing_0': [P_at_0],
                'chance_of_drawing_exactly_k': [P_at_exactly_k],
                'chance_of_drawing_at_most_k': [P_at_most_k],
                'chance_of_drawing_more_than_k': [P_more_than_k],
                'chance_of_drawing_at_least_k': [P_at_least_k],
                'chance_of_drawing_less_than_k': [P_less_than_k],
                'expected_successes_drawn': [CARDS_DRAWN * (NUM_SUCCESS_IN_DECK / (DECK_SIZE + CARDS_DRAWN)]
            })],
            ignore_index=True
        )
        )


        # Update variables for next turn
        TURN_NUMBER += 1
        DECK_SIZE -= CARDS_DRAWN

        # update remaining successes in deck based on expected successes drawn (law of large numbers)
        expected_successes_drawn = CARDS_DRAWN * (NUM_SUCCESS_IN_DECK / (DECK_SIZE + CARDS_DRAWN))
        NUM_SUCCESS_IN_DECK -= expected_successes_drawn

    # Sort by Turn_number
    df = df.sort_values(by='Turn_number').reset_index(drop=True)
    return df

print(probability_report(99, 40, 1, 1))