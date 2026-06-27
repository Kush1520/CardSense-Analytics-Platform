import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

from xgboost import XGBClassifier


df = pd.read_csv("../data/processed/fraud_clean.csv")


X = df.drop("class",axis=1)

y=df["class"]



X_train,X_test,y_train,y_test = train_test_split(

X,
y,

test_size=0.2,

random_state=42

)



model=XGBClassifier(

n_estimators=300,

max_depth=6,

learning_rate=0.05,

subsample=0.8


)



model.fit(

X_train,

y_train

)



pred=model.predict(X_test)



print(classification_report(

y_test,

pred

))



joblib.dump(

model,

"fraud_model.pkl"

)

print("Saved")