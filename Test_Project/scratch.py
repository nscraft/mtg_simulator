import pandas as pd

bf = pd.read_csv("records_battlefield.csv")


def max_turn():
    return bf["turn"].max()


final_bf = bf[bf["turn"] == max_turn()]

print(final_bf)
