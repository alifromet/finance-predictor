import yfinance as yf
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def predict_stock(ticker, period="6mo", interval="1d"):
    # Download data based on user choices
    df = yf.download(ticker, period=period, interval=interval)
    
    if df.empty:
        raise ValueError("No data fetched. Please check your ticker or select different period/interval.")

    # Create the target: will next candle be higher?
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
