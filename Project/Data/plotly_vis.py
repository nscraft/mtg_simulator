import dash
from dash import dcc, html, dash_table, Input, Output
import pandas as pd
from Project.Analytics.probability_engine import P_at_least_k

# === core probability logic ===
def generate_table_data(deck_size, num_successes, hit_bonus, hit_bonus_turn):
    rows = []
    cumulative_cards_drawn = 0
    cumulative_successes = 0

    for turn in range(0, 11):  # 11 rows
        # cards drawn this turn
        cards_drawn = 7 if turn == 0 else 1  # default rule: 7 on turn 0, then 1 each turn
        if turn == hit_bonus_turn:
            cards_drawn += hit_bonus

        cumulative_cards_drawn += cards_drawn

        # probability of drawing at least 1 success this turn
        p_at_least_1 = P_at_least_k(deck_size, num_successes, cards_drawn, 1)

        # expected successes drawn this turn
        expected_successes = cards_drawn * (num_successes / deck_size)

        cumulative_successes += expected_successes

        rows.append({
            "turn_number": turn,
            "num_cards_in_deck_turn_start": deck_size,
            "num_successes_in_deck_turn_start": num_successes,
            "cards_drawn_this_turn": cards_drawn,
            "cumulative_cards_drawn": cumulative_cards_drawn,
            "chance_of_drawing_at_least_1": p_at_least_1,
            "successes_drawn_this_turn": expected_successes,
            "cumulative_successes_drawn": cumulative_successes,
            "cumulative_success_as_percent_of_cumulative_cards_drawn":
                cumulative_successes / cumulative_cards_drawn if cumulative_cards_drawn > 0 else 0
        })

        # update deck for next turn
        deck_size -= cards_drawn
        num_successes -= expected_successes

    return pd.DataFrame(rows)


# === Dash App ===
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H2("Dynamic Probability Table"),

    html.Div([
        html.Label("Deck Size"),
        dcc.Slider(id="deck-size", min=20, max=120, step=1, value=99,
                   marks={i: str(i) for i in range(20, 121, 20)}),
        html.Label("Num Successes in Deck"),
        dcc.Slider(id="num-successes", min=0, max=99, step=1, value=40,
                   marks={i: str(i) for i in range(0, 101, 20)}),
        html.Label("Hit Bonus"),
        dcc.Slider(id="hit-bonus", min=0, max=10, step=1, value=0,
                   marks={i: str(i) for i in range(0, 11)}),
        html.Label("Hit Bonus Turn"),
        dcc.Slider(id="hit-bonus-turn", min=0, max=10, step=1, value=5,
                   marks={i: str(i) for i in range(0, 11)})
    ], style={"width": "70%", "margin": "20px"}),

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
    Input("hit-bonus", "value"),
    Input("hit-bonus-turn", "value")
)
def update_table(deck_size, num_successes, hit_bonus, hit_bonus_turn):
    df = generate_table_data(deck_size, num_successes, hit_bonus, hit_bonus_turn)
    return df.to_dict("records")


if __name__ == "__main__":
    app.run(debug=True)
