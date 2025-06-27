import streamlit as st
import stocks
import indices
import forex
import options

st.set_page_config(page_title="Finance Predictor", layout="wide")
st.title("📈 Finance Market Direction Predictor")

tab1, tab2, tab3, tab4 = st.tabs(["📊 Stocks", "🌐 Indices", "💱 Forex", "🧾 Options"])

# ---- STOCKS TAB ----
import streamlit as st
from app import stocks

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

# ---- INDICES TAB ----
with tab2:
    st.header("Index Prediction")
    index = st.selectbox("Select Index", ["^GSPC", "^IXIC", "^DJI"])

    if st.button("Predict Index"):
        df, direction, confidence, accuracy = indices.predict_index(index)
        st.line_chart(df["Close"])
        st.success(f"📈 **Prediction**: {direction}")
        st.info(f"🔢 **Confidence**: {confidence}%")
        st.info(f"🎯 **Model Accuracy**: {accuracy}%")

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
