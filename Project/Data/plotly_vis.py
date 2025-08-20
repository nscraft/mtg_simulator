import dash
from dash import dcc, html, dash_table, Input, Output, State
import pandas as pd
from Project.Analytics.probability_engine import P_at_least_k
import numpy as np


# === core probability logic ===

def generate_random_game_table_data(bonus_draws) -> pd.DataFrame:
    """Simulates drawing the same number of cards from multiple decks,
    each with a different number of successes, over 10 turns."""

    deck_size = 99  # Default deck size
    num_successes = [32, 34, 36, 38, 40]   # successes for each deck
    num_decks = len(num_successes)

    rows = []
    cumulative_cards_drawn = 0
    cumulative_successes = [0] * num_decks  # track per-deck totals

    for turn_number in range(0, 11):  # 11 rows
        turn_start_deck_size = deck_size
        turn_start_successes = num_successes.copy()
        successes_this_turn = [0] * num_decks

        # cards drawn this turn
        if turn_number == 0:
            cards_drawn_this_turn = 7
        else:
            cards_drawn_this_turn = 1 + bonus_draws.get(f"bonus-turn-{turn_number}", 0)

        # probability of at least 1 success this turn per deck
        p_at_least_1 = [
            P_at_least_k(N=deck_size, K=num_successes[i], n=cards_drawn_this_turn, k=1)
            for i in range(num_decks)
        ]

        # simulate draws
        for _ in range(cards_drawn_this_turn):
            for i in range(num_decks):
                p = P_at_least_k(N=deck_size, K=num_successes[i], n=1, k=1)
                hit = np.random.binomial(1, p)
                if hit:
                    num_successes[i] -= 1
                    successes_this_turn[i] += 1
            deck_size -= 1
            cumulative_cards_drawn += 1

        # update cumulative successes
        for i in range(num_decks):
            cumulative_successes[i] += successes_this_turn[i]

        # build row dictionary
        row = {
            "turn_number": turn_number,
            "num_cards_in_deck_turn_start": turn_start_deck_size,
            "cards_drawn_this_turn": cards_drawn_this_turn,
            "cumulative_cards_drawn": cumulative_cards_drawn,
        }

        # expand per-deck stats into row
        for i in range(num_decks):
            row[f"num_successes_in_deck_turn_start_deck{i+1}"] = turn_start_successes[i]
            row[f"chance_of_drawing_at_least_1_deck{i+1}"] = round(p_at_least_1[i], 2)
            row[f"simulated_successes_drawn_this_turn_deck{i+1}"] = successes_this_turn[i]
            row[f"cumulative_successes_drawn_deck{i+1}"] = cumulative_successes[i]
            row[f"cumulative_success_as_percent_of_cumulative_cards_drawn_deck{i+1}"] = (
                round(cumulative_successes[i] / cumulative_cards_drawn, 2)
                if cumulative_cards_drawn > 0 else 0
            )

        rows.append(row)

    return pd.DataFrame(rows)


def generate_monte_carlo_table_data(bonus_draws, num_trials: int = 100) -> pd.DataFrame:
    """
    Simulates drawing cards from multiple decks over 11 turns, repeated num_trials times.
    Returns the average outcome per turn across all trials.
    """

    num_successes_init = [32, 34, 36, 38, 40]  # starting successes per deck
    num_decks = len(num_successes_init)

    all_trials = []

    for trial in range(num_trials):
        deck_size = 99
        num_successes = num_successes_init.copy()
        cumulative_cards_drawn = 0
        cumulative_successes = [0] * num_decks
        rows = []

        for turn_number in range(0, 11):
            turn_start_deck_size = deck_size
            turn_start_successes = num_successes.copy()
            successes_this_turn = [0] * num_decks

            # cards drawn this turn
            if turn_number == 0:
                cards_drawn_this_turn = 7
            else:
                cards_drawn_this_turn = 1 + bonus_draws.get(f"bonus-turn-{turn_number}", 0)

            # probability of at least 1 success this turn
            p_at_least_1 = [
                P_at_least_k(N=deck_size, K=num_successes[i], n=cards_drawn_this_turn, k=1)
                for i in range(num_decks)
            ]

            # simulate draws
            for _ in range(cards_drawn_this_turn):
                for i in range(num_decks):
                    p = P_at_least_k(N=deck_size, K=num_successes[i], n=1, k=1)
                    hit = np.random.binomial(1, p)
                    if hit:
                        num_successes[i] -= 1
                        successes_this_turn[i] += 1
                deck_size -= 1
                cumulative_cards_drawn += 1

            # update cumulative successes
            for i in range(num_decks):
                cumulative_successes[i] += successes_this_turn[i]

            # build row
            row = {
                "trial": trial,
                "turn_number": turn_number,
                "num_cards_in_deck_turn_start": turn_start_deck_size,
                "cards_drawn_this_turn": cards_drawn_this_turn,
                "cumulative_cards_drawn": cumulative_cards_drawn,
            }
            for i in range(num_decks):
                row[f"num_successes_in_deck_turn_start_deck{i+1}"] = turn_start_successes[i]
                row[f"chance_of_drawing_at_least_1_deck{i+1}"] = round(p_at_least_1[i], 2)
                row[f"simulated_successes_drawn_this_turn_deck{i+1}"] = successes_this_turn[i]
                row[f"cumulative_successes_drawn_deck{i+1}"] = cumulative_successes[i]
                row[f"cumulative_success_as_percent_of_cumulative_cards_drawn_deck{i+1}"] = (
                    round(cumulative_successes[i] / cumulative_cards_drawn, 2)
                    if cumulative_cards_drawn > 0 else 0
                )
            rows.append(row)

        all_trials.extend(rows)

    # Combine all trials
    df_all = pd.DataFrame(all_trials)

    # Average across trials, grouped by turn_number
    df_avg = df_all.groupby("turn_number").mean(numeric_only=True).reset_index()

    return df_avg


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
    df = generate_random_game_table_data(bonus_dict)

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
