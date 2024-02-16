import pandas as pd

# Create the DataFrame
mydf = pd.DataFrame({
    "game": [1, 1, 1, 1, 2, 2, 2, 2],
    "turn": [1, 1, 2, 2, 1, 1, 2, 2],
    "card_score": [0, 0, 1, 1, 1, 1, 0, 0]
})

# Filter the DataFrame where turn is equal to 2, then group by 'game' and sum 'card_score'
result = mydf[mydf['turn'] == 2].groupby('game')['card_score'].sum().reset_index()

print(result.card_score.mean())
