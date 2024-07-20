import pandas as pd
df = pd.read_csv('data/raw_card_transdata.csv')
split_df = df.sample(frac = 0.7)
rest_df = df.drop(split_df.index)

split_df.to_csv("data/card_transdata.csv", encoding='utf-8', index=False, header=True)
rest_df.to_csv("data/future_card_transdata.csv", encoding='utf-8', index=False, header=True)