# app/stocks.py

import yfinance as yf
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def predict_stock(ticker):
    # Download last 6 months of daily stock data
    df = yf.download(ticker, period="6mo", interval="1d")

    # Add target column: 1 if next day's close is higher, else 0
    df["Target"] = (df["Close"].shift(-1) > df["Close"]).astype(int)
    df.dropna(inplace=True)

    # Use these columns for prediction
    features = ["Open", "High", "Low", "Close", "Volume"]
    X = df[features]
    y = df["Target"]

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False)

    # Train model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Predict next movement
    last_data = X.tail(1)
    prediction = model.predict(last_data)[0]
    probability = model.predict_proba(last_data)[0]
    direction = "UP" if prediction == 1 else "DOWN"
    confidence = round(max(probability) * 100, 2)

    # Calculate accuracy on test data
    accuracy = round(accuracy_score(y_test, model.predict(X_test)) * 100, 2)

    return df, direction, confidence, accuracy
