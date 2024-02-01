import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Create a DataFrame with one column 'mana_value'
deck_df1 = pd.DataFrame({
    'card_slot': range(1, 100),
    'score': np.random.randint(1, 11, size=99),
    'island': np.random.randint(0, 2, size=99),
    'mana_cost': np.random.randint(0, 10, size=99)
})

deck_df2 = pd.DataFrame({
    'card_slot': range(1, 99),
    'score': np.random.randint(1, 11, size=98),
    'island': np.random.randint(0, 2, size=98),
    'mana_cost': np.random.randint(0, 10, size=98)
})

print(deck_df1)
print(deck_df2)

# BE VERY CAREFUL NOT TO OVERWRITE SOURCE FILES
deck_df1.to_excel('rand_deck_1.xlsx')
deck_df2.to_excel('rand_deck_2.xlsx')
