from app import stocks
from app import indices
from app import forex
from app import options


st.set_page_config(page_title="Finance Predictor", layout="wide")
st.title("📈 Finance Market Direction Predictor")

tab1, tab2, tab3, tab4 = st.tabs(["📊 Stocks", "🌐 Indices", "💱 Forex", "🧾 Options"])

# ---- STOCKS TAB ----
st.title("📈 Finance Market Direction Predictor")

ticker = st.text_input("Enter Stock Ticker (e.g., AAPL, TSLA)", "AAPL")

period = st.selectbox("Select data period", ["1d", "5d", "7d", "1mo", "3mo", "6mo"])
interval = st.selectbox("Select interval", ["1m", "5m", "15m", "30m", "1h", "1d"])

if st.button("Predict Stock"):
    df, direction, confidence, accuracy = stocks.predict_stock(ticker, period, interval)
    st.line_chart(df["Close"])
    st.success(f"📈 **Prediction**: {direction}")
    st.info(f"🔢 **Confidence**: {confidence}%")
    st.info(f"🎯 **Model Accuracy**: {accuracy}%")

import streamlit as st
from app import indices  # your indices.py with predict_index function

def indices_tab():
    st.header("📊 Indices Prediction")

    indices_options = {
        "S&P 500": "^GSPC",
        "Dow Jones": "^DJI",
        "Nasdaq Composite": "^IXIC",
        "Russell 2000": "^RUT",
        "FTSE 100": "^FTSE",
        "DAX (Germany)": "^GDAXI",
        "CAC 40 (France)": "^FCHI",
        "Nikkei 225 (Japan)": "^N225",
        "Hang Seng (Hong Kong)": "^HSI",
        "ASX 200 (Australia)": "^AXJO",
        "TSX Composite (Canada)": "^GSPTSE",
    }

    selected_index_name = st.selectbox("Select an Index to Predict", list(indices_options.keys()))
    selected_index_symbol = indices_options[selected_index_name]

    if st.button("Predict Index"):
        try:
            df, direction, confidence, accuracy = indices.predict_index(selected_index_symbol)
            st.line_chart(df["Close"])
            st.success(f"Prediction: **{direction}**")
            st.info(f"Confidence: {confidence}%")
            st.info(f"Model Accuracy: {accuracy}%")
        except Exception as e:
            st.error(f"Error: {e}")

# Then in your main.py you call indices_tab() where you render the indices section.


# ---- FOREX TAB ----
with tab3:
    st.header("Forex Prediction")
    from_currency = st.text_input("From Currency (e.g., USD)", "USD")
    to_currency = st.text_input("To Currency (e.g., EUR)", "EUR")

    if st.button("Predict Forex"):
        df, direction, confidence, accuracy = forex.predict_forex(from_currency, to_currency)
        st.line_chart(df["Close"])
        st.success(f"📈 **Prediction**: {direction}")
        st.info(f"🔢 **Confidence**: {confidence}%")
        st.info(f"🎯 **Model Accuracy**: {accuracy}%")

# ---- OPTIONS TAB ----
with tab4:
    st.header("Options Prediction")
    option_ticker = st.text_input("Enter Underlying Ticker (e.g., AAPL)", "AAPL")

    if st.button("Predict Option"):
        df, direction, confidence, accuracy = options.predict_option(option_ticker)
        st.line_chart(df["Close"])
        st.success(f"📈 **Prediction**: {direction}")
        st.info(f"🔢 **Confidence**: {confidence}%")
        st.info(f"🎯 **Model Accuracy**: {accuracy}%")
try:
    df, direction, confidence, accuracy = stocks.predict_stock(ticker, period, interval)
except ValueError as e:
    st.error(f"⚠️ {e}")
    st.stop()
