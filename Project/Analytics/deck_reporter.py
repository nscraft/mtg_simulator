from Project.Data.probability_report import probability_report

def deck_reporter(deck_name, deck_metrics, opening_hand_probs):
    probability_report(
        pop_size=deck_metrics.deck_library_count(),
        successes=deck_metrics.num_land(),
        sample_size=1,
        successes_in_sample=1,
        success_method='at_least_k'
    )
    report = (
        f"{deck_name}\n"
        f"Deck Stats:\n"
        f"{deck_metrics.num_commander()} commander(s) with {deck_metrics.deck_library_count()} cards in library.\n"
        f"Total of {deck_metrics.num_land()} lands.\n"
        f"Average mana cost of non-land cards is {deck_metrics.avg_mana_cost()}.\n"
        f"Total number of ramp cards is {deck_metrics.num_ramp()} and total number of draw cards is {deck_metrics.num_draw()}.\n"
        f"The average ramp value is {deck_metrics.avg_ramp_value()} and the average draw value is {deck_metrics.avg_draw_value()}.\n"
        f"There are {deck_metrics.num_other()} other (aka: "
        f"noncommander, nonland, nonramp, nondraw) cards.\n"
        f"Average score of cards in deck is {deck_metrics.avg_card_score()}.\n"
        f"Probabilities:\n"
        f"{round(opening_hand_probs.twothree_land_opener() * 100, 1)}% chance of drawing 2-3 land on turn 1?\n"
        f"{round(opening_hand_probs.fourormore_land_opener() * 100, 1)}% chance of starting with 4 or more lands.\n"
        f"{round(opening_hand_probs.zero_land_opener() * 100, 1)}% chance of starting with zero land.\n"
        f"{round(opening_hand_probs.five_unplayable_opener() * 100, 1)}% chance of drawing 5 or more nonland cards "
        f"Turn over turn, probability report saved to csv in ./Project/Data/\n"
    )
    return report
