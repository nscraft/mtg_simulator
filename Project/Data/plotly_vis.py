import dash
from dash import dcc, html, dash_table, Input, Output, State
import pandas as pd
from Project.Analytics.probability_engine import P_at_least_k
import numpy as np


# === core probability logic ===
def generate_table_data(deck_size: int, num_success_in_deck: int, bonus_draws) -> pd.DataFrame:
    rows = []
    cumulative_cards_drawn = 0
    cumulative_successes_drawn = 0

    for turn_number in range(0, 11):  # 11 rows
        turn_start_deck_size = deck_size
        turn_start_num_successes = num_success_in_deck
        successes_drawn_this_turn = 0

        # cards drawn this turn
        if turn_number == 0:
            cards_drawn_this_turn = 7
        else:
            # 1 plus slider value for bonus draws
            cards_drawn_this_turn = 1 + bonus_draws.get(f"bonus-turn-{turn_number}", 0)

        cumulative_cards_drawn += cards_drawn_this_turn

        # probability of drawing at least 1 success this turn
        p_at_least_1 = P_at_least_k(turn_start_deck_size, turn_start_num_successes, cards_drawn_this_turn, 1)

        # Simulate drawing cards
        for _ in range(cards_drawn_this_turn):
            p_at_least_1 = P_at_least_k(
                N=deck_size, K=num_success_in_deck, n=1, k=1)
            hit_result = np.random.binomial(1, P_at_least_k)
            deck_size -= 1
            cumulative_cards_drawn += 1
            if hit_result == 1:
                num_success_in_deck -= 1
                successes_drawn_this_turn += 1

        # Update cumulative trackers
        cumulative_successes_drawn += successes_drawn_this_turn

        rows.append({
            "turn_number": turn_number,
            "num_cards_in_deck_turn_start": turn_start_deck_size,
            "num_successes_in_deck_turn_start": turn_start_num_successes,
            "cards_drawn_this_turn": cards_drawn_this_turn,
            "cumulative_cards_drawn": cumulative_cards_drawn,
            "chance_of_drawing_at_least_1": round(p_at_least_1, 2),
            "successes_drawn_this_turn": successes_drawn_this_turn,
            "cumulative_successes_drawn": cumulative_successes_drawn,
            "cumulative_success_as_percent_of_cumulative_cards_drawn":
                round(cumulative_successes_drawn / cumulative_cards_drawn if cumulative_cards_drawn > 0 else 0, 2)
        })

        # update deck for next turn
        turn_number += 1

    return pd.DataFrame(rows)


# === Dash App ===
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H2("Dynamic Probability Table"),

    html.Div([
        html.Label("Deck Size"),
        dcc.Input(id="deck-size", type="number", value=99, min=1, step=1),

        html.Label("Num Successes in Deck"),
        dcc.Slider(
            id="num-successes",
            min=0, max=99, step=1, value=40,
            marks={i: str(i) for i in range(0, 101, 20)},
            tooltip={"placement": "bottom", "always_visible": True}
        ),
    ], style={"width": "70%", "margin": "20px"}),

    html.H4("Bonus Draw"),

    html.Div(
        [
            dcc.Slider(
                id=f"bonus-turn-{i}",
                min=0, max=10, step=1, value=0,
                vertical=True,
                tooltip={"placement": "left", "always_visible": True}
            )
            for i in range(1, 11)
        ],
        style={"display": "flex", "justifyContent": "space-around",
               "alignItems": "flex-end", "height": "300px", "marginBottom": "30px"}
    ),

    dash_table.DataTable(
        id="prob-table",
        columns=[{"name": c, "id": c} for c in [
            'turn_number',
            'num_cards_in_deck_turn_start',
            'num_successes_in_deck_turn_start',
            'cards_drawn_this_turn',
            'cumulative_cards_drawn',
            'chance_of_drawing_at_least_1',
            'successes_drawn_this_turn',
            'cumulative_successes_drawn',
            'cumulative_success_as_percent_of_cumulative_cards_drawn']],
        style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'center', 'padding': '5px'},
        style_header={'backgroundColor': '#f4f4f4', 'fontWeight': 'bold'},
    )
])


# === callback ===
@app.callback(
    Output("prob-table", "data"),
    Input("deck-size", "value"),
    Input("num-successes", "value"),
    [Input(f"bonus-turn-{i}", "value") for i in range(1, 11)]
)
def update_table(deck_size, num_successes, *bonus_draws):
    df = generate_table_data(deck_size, num_successes, bonus_draws)
    return df.to_dict("records")


if __name__ == "__main__":
    app.run(debug=True)
