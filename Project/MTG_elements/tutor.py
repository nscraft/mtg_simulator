import random
import pandas as pd


def pick_card(card_pool, num_card):
    if isinstance(card_pool, pd.Series):
        card_pool = card_pool.tolist()
    if num_card > len(card_pool):
        raise ValueError("Number of cards to pick exceeds the available cards in the pool.")
    picked_cards = set()
    while len(picked_cards) < num_card:
        card = random.choice(card_pool)
        picked_cards.add(card)
    return picked_cards
