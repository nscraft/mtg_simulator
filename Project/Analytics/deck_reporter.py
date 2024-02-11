def deck_reporter(deck_name, deck_metrics, opening_hand_probs):  # will need to add a deck name argument later
    report = (
        f"{deck_name}\n"
        f"Deck Stats:\n"
        f"{deck_metrics.num_commander()} commander(s) with {deck_metrics.deck_library_count()} cards in library.\n"
        f"Total of {deck_metrics.num_land()} lands.\n"
        f"Average mana cost of non-land cards is {deck_metrics.avg_mana_cost()}.\n"
        f"Total number of ramp cards is {deck_metrics.num_ramp()} and total number of key cards is {deck_metrics.num_key()}.\n"
        f"The average ramp value is {deck_metrics.avg_ramp_value()} and the average key value is {deck_metrics.avg_key_value()}.\n"
        f"There are {deck_metrics.num_other()} other (aka: "
        f"noncommander, nonland, nonramp, nonkey) cards.\n"
        f"Probabilities:\n"
        f"{round(opening_hand_probs.twothree_land_opener() * 100, 1)}% chance of drawing 2-3 land on turn 1?\n"
        f"{round(opening_hand_probs.fourormore_land_opener() * 100, 1)}% chance of starting with 4 or more lands.\n"
        f"{round(opening_hand_probs.zero_land_opener() * 100, 1)}% chance of starting with zero land.\n"
        f"{round(opening_hand_probs.five_unplayable_opener() * 100, 1)}% chance of drawing 5 or more nonland cards "
        f"that cost more than 1 mana on turn 1?\n"
        f"Probability of drawing playable ramp by turn 2?\n"
        f"Probability of drawing playable key card by turn 4?\n"
    )
    return report
