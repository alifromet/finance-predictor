# app/forex.py

import yfinance as yf
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def predict_forex(from_currency, to_currency):
    pair = f"{from_currency}{to_currency}=X"
    df = yf.download(pair, period="6mo", interval="1d")

    if df.empty:
        raise ValueError(f"Invalid or unavailable forex pair: {pair}")

    df["Target"] = (df["Close"].shift(-1) > df["Close"]).astype(int)
    df.dropna(inplace=True)

    features = ["Open", "High", "Low", "Close", "Volume"]
    X = df[features]
    y = df["Target"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    last_data = X.tail(1)
    prediction = model.predict(last_data)[0]
    probability = model.predict_proba(last_data)[0]
    direction = "UP" if prediction == 1 else "DOWN"
    confidence = round(max(probability) * 100, 2)
    accuracy = round(accuracy_score(y_test, model.predict(X_test)) * 100, 2)

    return df, direction, confidence, accuracy


