import dash
from dash import dcc, html, dash_table, Input, Output, State
import pandas as pd
from Project.Analytics.probability_engine import P_at_least_k
import numpy as np


# === core probability logic ===
def generate_table_data(bonus_draws) -> pd.DataFrame:
    """Simulates drawing the same number of cards from 5 decks, each with a different number of successes over 10 turns."""

    deck_size = 99  # Default deck size
    num_success_in_deck1 = 32
    num_success_in_deck2 = 34
    num_success_in_deck3 = 36
    num_success_in_deck4 = 38
    num_success_in_deck5 = 40
    rows = []
    cumulative_cards_drawn = 0
    cumulative_successes_drawn_deck1 = 0
    cumulative_successes_drawn_deck2 = 0
    cumulative_successes_drawn_deck3 = 0
    cumulative_successes_drawn_deck4 = 0
    cumulative_successes_drawn_deck5 = 0

    for turn_number in range(0, 11):  # 11 rows
        turn_start_deck_size = deck_size
        turn_start_num_successes_deck1 = num_success_in_deck1
        turn_start_num_successes_deck2 = num_success_in_deck2
        turn_start_num_successes_deck3 = num_success_in_deck3
        turn_start_num_successes_deck4 = num_success_in_deck4
        turn_start_num_successes_deck5 = num_success_in_deck5
        successes_drawn_this_turn_deck1 = 0
        successes_drawn_this_turn_deck2 = 0
        successes_drawn_this_turn_deck3 = 0
        successes_drawn_this_turn_deck4 = 0
        successes_drawn_this_turn_deck5 = 0

        # cards drawn this turn
        if turn_number == 0:
            cards_drawn_this_turn = 7
        else:
            # 1 plus slider value for bonus draws
            cards_drawn_this_turn = 1 + bonus_draws.get(f"bonus-turn-{turn_number}", 0)

        # probability of drawing at least 1 success this turn
        p_at_least_1_deck1 = P_at_least_k(N=deck_size, K=num_success_in_deck1, n=cards_drawn_this_turn, k=1)
        p_at_least_1_deck2 = P_at_least_k(N=deck_size, K=num_success_in_deck2, n=cards_drawn_this_turn, k=1)
        p_at_least_1_deck3 = P_at_least_k(N=deck_size, K=num_success_in_deck3, n=cards_drawn_this_turn, k=1)
        p_at_least_1_deck4 = P_at_least_k(N=deck_size, K=num_success_in_deck4, n=cards_drawn_this_turn, k=1)
        p_at_least_1_deck5 = P_at_least_k(N=deck_size, K=num_success_in_deck5, n=cards_drawn_this_turn, k=1)

        # Simulate drawing cards
        for _ in range(cards_drawn_this_turn):
            probability1 = P_at_least_k(N=deck_size, K=num_success_in_deck1, n=1, k=1)
            probability2 = P_at_least_k(N=deck_size, K=num_success_in_deck2, n=1, k=1)
            probability3 = P_at_least_k(N=deck_size, K=num_success_in_deck3, n=1, k=1)
            probability4 = P_at_least_k(N=deck_size, K=num_success_in_deck4, n=1, k=1)
            probability5 = P_at_least_k(N=deck_size, K=num_success_in_deck5, n=1, k=1)
            hit_result1 = np.random.binomial(1, probability1)
            hit_result2 = np.random.binomial(1, probability2)
            hit_result3 = np.random.binomial(1, probability3)
            hit_result4 = np.random.binomial(1, probability4)
            hit_result5 = np.random.binomial(1, probability5)
            deck_size -= 1
            cumulative_cards_drawn += 1
            if hit_result1 == 1:
                num_success_in_deck1 -= 1
                successes_drawn_this_turn_deck1 += 1
            if hit_result2 == 1:
                num_success_in_deck2 -= 1
                successes_drawn_this_turn_deck2 += 1
            if hit_result3 == 1:
                num_success_in_deck3 -= 1
                successes_drawn_this_turn_deck3 += 1
            if hit_result4 == 1:
                num_success_in_deck4 -= 1
                successes_drawn_this_turn_deck4 += 1
            if hit_result5 == 1:
                num_success_in_deck5 -= 1
                successes_drawn_this_turn_deck5 += 1

        # Update cumulative trackers
        cumulative_successes_drawn_deck1 += successes_drawn_this_turn_deck1
        cumulative_successes_drawn_deck2 += successes_drawn_this_turn_deck2
        cumulative_successes_drawn_deck3 += successes_drawn_this_turn_deck3
        cumulative_successes_drawn_deck4 += successes_drawn_this_turn_deck4
        cumulative_successes_drawn_deck5 += successes_drawn_this_turn_deck5

        rows.append({
            "turn_number": turn_number,
            "num_cards_in_deck_turn_start": turn_start_deck_size,
            "num_successes_in_deck_turn_start_deck1": turn_start_num_successes_deck1,
            "num_successes_in_deck_turn_start_deck2": turn_start_num_successes_deck2,
            "num_successes_in_deck_turn_start_deck3": turn_start_num_successes_deck3,
            "num_successes_in_deck_turn_start_deck4": turn_start_num_successes_deck4,
            "num_successes_in_deck_turn_start_deck5": turn_start_num_successes_deck5,
            "cards_drawn_this_turn": cards_drawn_this_turn,
            "cumulative_cards_drawn": cumulative_cards_drawn,
            "chance_of_drawing_at_least_1_deck1": round(p_at_least_1_deck1, 2),
            "chance_of_drawing_at_least_1_deck2": round(p_at_least_1_deck2, 2),
            "chance_of_drawing_at_least_1_deck3": round(p_at_least_1_deck3, 2),
            "chance_of_drawing_at_least_1_deck4": round(p_at_least_1_deck4, 2),
            "chance_of_drawing_at_least_1_deck5": round(p_at_least_1_deck5, 2),
            "simulated_successes_drawn_this_turn_deck1": successes_drawn_this_turn_deck1,
            "simulated_successes_drawn_this_turn_deck2": successes_drawn_this_turn_deck2,
            "simulated_successes_drawn_this_turn_deck3": successes_drawn_this_turn_deck3,
            "simulated_successes_drawn_this_turn_deck4": successes_drawn_this_turn_deck4,
            "simulated_successes_drawn_this_turn_deck5": successes_drawn_this_turn_deck5,
            "cumulative_successes_drawn_deck1": cumulative_successes_drawn_deck1,
            "cumulative_successes_drawn_deck2": cumulative_successes_drawn_deck2,
            "cumulative_successes_drawn_deck3": cumulative_successes_drawn_deck3,
            "cumulative_successes_drawn_deck4": cumulative_successes_drawn_deck4,
            "cumulative_successes_drawn_deck5": cumulative_successes_drawn_deck5,
            "cumulative_success_as_percent_of_cumulative_cards_drawn_deck1":
                round(cumulative_successes_drawn_deck1 / cumulative_cards_drawn if cumulative_cards_drawn > 0 else 0, 2),
            "cumulative_success_as_percent_of_cumulative_cards_drawn_deck2":
                round(cumulative_successes_drawn_deck2 / cumulative_cards_drawn if cumulative_cards_drawn > 0 else 0, 2),
            "cumulative_success_as_percent_of_cumulative_cards_drawn_deck3":
                round(cumulative_successes_drawn_deck3 / cumulative_cards_drawn if cumulative_cards_drawn > 0 else 0, 2),
            "cumulative_success_as_percent_of_cumulative_cards_drawn_deck4":
                round(cumulative_successes_drawn_deck4 / cumulative_cards_drawn if cumulative_cards_drawn > 0 else 0, 2),
            "cumulative_success_as_percent_of_cumulative_cards_drawn_deck5":
                round(cumulative_successes_drawn_deck5 / cumulative_cards_drawn if cumulative_cards_drawn > 0 else 0, 2)
        })

    return pd.DataFrame(rows)


# === Dash App ===
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H2("Dynamic Probability Table"),
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
            'num_successes_in_deck_turn_start_deck1',
            'num_successes_in_deck_turn_start_deck2',
            'num_successes_in_deck_turn_start_deck3',
            'num_successes_in_deck_turn_start_deck4',
            'cards_drawn_this_turn',
            'cumulative_cards_drawn',
            'chance_of_drawing_at_least_1_deck1',
            'chance_of_drawing_at_least_1_deck2',
            'chance_of_drawing_at_least_1_deck3',
            'chance_of_drawing_at_least_1_deck4',
            'chance_of_drawing_at_least_1_deck5',
            'simulated_successes_drawn_this_turn_deck1',
            'simulated_successes_drawn_this_turn_deck2',
            'simulated_successes_drawn_this_turn_deck3',
            'simulated_successes_drawn_this_turn_deck4',
            'simulated_successes_drawn_this_turn_deck5',
            'cumulative_successes_drawn_deck1',
            'cumulative_successes_drawn_deck2',
            'cumulative_successes_drawn_deck3',
            'cumulative_successes_drawn_deck4',
            'cumulative_successes_drawn_deck5',
            'cumulative_success_as_percent_of_cumulative_cards_drawn_deck1',
            'cumulative_success_as_percent_of_cumulative_cards_drawn_deck2',
            'cumulative_success_as_percent_of_cumulative_cards_drawn_deck3',
            'cumulative_success_as_percent_of_cumulative_cards_drawn_deck4',
            'cumulative_success_as_percent_of_cumulative_cards_drawn_deck5'
        ]],
        style_table={"overflowX": "auto", "maxWidth": "100%"},
        style_cell={'textAlign': 'center', 'padding': '6px'},
        style_header={'backgroundColor': '#f4f4f4', 'fontWeight': 'bold'},
    )
])

# === callback ===
@app.callback(
    [Output("prob-table", "data"),
     Output("prob-table", "style_data_conditional")],
    [Input(f"bonus-turn-{i}", "value") for i in range(1, 11)]
)
def update_table(*bonus_draws):
    bonus_dict = {f"bonus-turn-{i+1}": val for i, val in enumerate(bonus_draws)}
    df = generate_table_data(bonus_dict)

    # Conditional formatting rules
    style_data_conditional = []

    # Formatting for "chance_of_drawing_at_least_1..."
    for column in [
        'chance_of_drawing_at_least_1_deck1',
        'chance_of_drawing_at_least_1_deck2',
        'chance_of_drawing_at_least_1_deck3',
        'chance_of_drawing_at_least_1_deck4',
        'chance_of_drawing_at_least_1_deck5'
    ]:
        for i, row in df.iterrows():
            value = row[column]
            fill_percentage = int(value * 100)
            style_data_conditional.append({
                "if": {"row_index": i, "column_id": column},
                "background": f"linear-gradient(to right, #2196F3 {fill_percentage}%, transparent {fill_percentage}%)",
                "color": "black"
            })

    # Formatting for "simulated_successes_drawn_this_turn..."
    for column in [
        'simulated_successes_drawn_this_turn_deck1',
        'simulated_successes_drawn_this_turn_deck2',
        'simulated_successes_drawn_this_turn_deck3',
        'simulated_successes_drawn_this_turn_deck4',
        'simulated_successes_drawn_this_turn_deck5'
    ]:
        max_value = df[column].max()
        if max_value > 0:  # Avoid division by zero
            for i, row in df.iterrows():
                value = row[column]
                fill_percentage = int((value / max_value) * 100)
                style_data_conditional.append({
                    "if": {"row_index": i, "column_id": column},
                    "background": f"linear-gradient(to right, #4CAF50 {fill_percentage}%, transparent {fill_percentage}%)",
                    "color": "black"
                })

    # Formatting for "cumulative_successes_drawn..."
    for column in [
        'cumulative_successes_drawn_deck1',
        'cumulative_successes_drawn_deck2',
        'cumulative_successes_drawn_deck3',
        'cumulative_successes_drawn_deck4',
        'cumulative_successes_drawn_deck5'
    ]:
        max_value = df[column].max()
        if max_value > 0:  # Avoid division by zero
            for i, row in df.iterrows():
                value = row[column]
                fill_percentage = int((value / max_value) * 100)
                style_data_conditional.append({
                    "if": {"row_index": i, "column_id": column},
                    "background": f"linear-gradient(to right, #4CAF50 {fill_percentage}%, transparent {fill_percentage}%)",
                    "color": "black"
                })

    # Formatting for "cumulative_success_as_percent_of_cumulative_cards_drawn..."
    for column in [
        'cumulative_success_as_percent_of_cumulative_cards_drawn_deck1',
        'cumulative_success_as_percent_of_cumulative_cards_drawn_deck2',
        'cumulative_success_as_percent_of_cumulative_cards_drawn_deck3',
        'cumulative_success_as_percent_of_cumulative_cards_drawn_deck4',
        'cumulative_success_as_percent_of_cumulative_cards_drawn_deck5'
    ]:
        for i, row in df.iterrows():
            value = row[column]
            fill_percentage = int(value * 100)
            style_data_conditional.append({
                "if": {"row_index": i, "column_id": column},
                "background": f"linear-gradient(to right, #FF9800 {fill_percentage}%, transparent {fill_percentage}%)",
                "color": "black"
            })

    return df.to_dict("records"), style_data_conditional


if __name__ == "__main__":
    app.run(debug=True)
