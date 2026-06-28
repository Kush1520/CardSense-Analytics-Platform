import pandas as pd
import joblib

model = joblib.load("fraud_model.pkl")

df = pd.read_csv("../data/processed/fraud_clean.csv")

pred = model.predict(df.drop("class", axis=1))
proba = model.predict_proba(df.drop("class", axis=1))

result = pd.DataFrame({
    'amount': df['amount'],
    'actual_class': df['class'],
    'prediction': pred,
    'fraud_probability': proba[:,1]
}) 

result.to_csv("fraud_dashboard.csv", index=False)

print("Dashboard file created")