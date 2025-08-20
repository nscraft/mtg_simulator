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

        # probability of drawing at least 1 success this turn
        p_at_least_1 = P_at_least_k(N=deck_size, K=num_success_in_deck, n=cards_drawn_this_turn, k=1)

        # Simulate drawing cards
        for _ in range(cards_drawn_this_turn):
            probability = P_at_least_k(N=deck_size, K=num_success_in_deck, n=1, k=1)
            hit_result = np.random.binomial(1, probability)
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

    return pd.DataFrame(rows)


# === Dash App ===
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H2("Dynamic Probability Table"),

    # ── Controls row ────────────────────────────────────────────────────────────
    html.Div([
        html.Div([
            html.Label("Deck Size"),
            dcc.Input(
                id="deck-size",
                type="number",
                value=99,
                min=1,
                step=1,
                style={"width": "100%"}
            ),
        ], style={
            "display": "flex",
            "flexDirection": "column",
            "minWidth": "60px",
            "maxWidth": "80px"
        }),

        html.Div([
            html.Label("Num Successes in Deck"),
            dcc.Slider(
                id="num-successes",
                min=0, max=99, step=1, value=38,
                marks={i: str(i) for i in range(0, 101, 10)},
                tooltip={"placement": "right", "always_visible": True},
            )
        ], style={"maxWidth": "400px", "width": "100%"}),
    ], style={"display": "flex", "alignItems": "center", "marginBottom": "30px"}),

    html.H4("Bonus Draw", style={"marginTop": "8px", "marginBottom": "8px"}),

    # ── Bonus sliders row (turns 1–10) ─────────────────────────────────────────
    html.Div([
        html.Div([
            dcc.Slider(
                id=f"bonus-turn-{i}",
                min=0, max=10, step=1, value=0,
                vertical=True,
                verticalHeight=60,
                tooltip={"placement": "left", "always_visible": False},
                marks=None
            ),
            html.Div(f"T{i}", style={"marginTop": "6px", "textAlign": "center"})
        ], style={
            "display": "flex",
            "flexDirection": "column",
            "alignItems": "center",
            "width": "40px"
        })
        for i in range(1, 11)
    ], style={
        "display": "flex",
        "gap": "12px",
        "justifyContent": "left",
        "alignItems": "flex-end",
        "marginBottom": "24px",
        "flexWrap": "nowrap",
        "overflowX": "auto",  # horizontal scroll if screen is narrow
        "paddingBottom": "4px"
    }),

    # ── Table ──────────────────────────────────────────────────────────────────
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
        style_table={"overflowX": "auto", "maxWidth": "100%"},
        style_cell={'textAlign': 'center', 'padding': '6px'},
        style_header={'backgroundColor': '#f4f4f4', 'fontWeight': 'bold'},
    )
])

# === callback ===
@app.callback(
    [Output("prob-table", "data"),
     Output("prob-table", "style_data_conditional")],
    Input("deck-size", "value"),
    Input("num-successes", "value"),
    [Input(f"bonus-turn-{i}", "value") for i in range(1, 11)]
)
def update_table(deck_size, num_successes, *bonus_draws):
    bonus_dict = {f"bonus-turn-{i+1}": val for i, val in enumerate(bonus_draws)}
    df = generate_table_data(deck_size, num_successes, bonus_dict)

    # Conditional formatting rules
    style_data_conditional = []

    # Formatting for "successes_drawn_this_turn"
    max_value = df["successes_drawn_this_turn"].max()
    if max_value > 0:  # Avoid division by zero
        for i, row in df.iterrows():
            value = row["successes_drawn_this_turn"]
            fill_percentage = int((value / max_value) * 100)
            style_data_conditional.append({
                "if": {"row_index": i, "column_id": "successes_drawn_this_turn"},
                "background": f"linear-gradient(to right, #4CAF50 {fill_percentage}%, transparent {fill_percentage}%)",
                "color": "black"
            })

    # Formatting for "chance_of_drawing_at_least_1"
    for i, row in df.iterrows():
        value = row["chance_of_drawing_at_least_1"]
        red = int((1 - value) * 255)
        green = int(value * 255)
        style_data_conditional.append({
            "if": {"row_index": i, "column_id": "chance_of_drawing_at_least_1"},
            "backgroundColor": f"rgb({red}, {green}, 0)",
            "color": "black"
        })

    return df.to_dict("records"), style_data_conditional


if __name__ == "__main__":
    app.run(debug=True)
