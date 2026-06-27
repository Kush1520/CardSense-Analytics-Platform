import pandas as pd

df = pd.read_csv("fraud_predictions.csv")

print(df.head())

print()

print(df['prediction'].value_counts())

print()

print(df['fraud_probability'].describe())