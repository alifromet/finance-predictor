import streamlit as st
import yfinance as yf

def show():
    st.header("💱 Forex Exchange Rates")

    pairs = {
        "EUR/USD": "EURUSD=X",
        "USD/JPY": "USDJPY=X",
        "GBP/USD": "GBPUSD=X",
        "USD/CHF": "USDCHF=X",
        "AUD/USD": "AUDUSD=X",
        "USD/CAD": "USDCAD=X",
        "EUR/GBP": "EURGBP=X"
    }

    selected_pair = st.selectbox("Select Currency Pair", list(pairs.keys()))
    symbol = pairs[selected_pair]

    data = yf.Ticker(symbol).history(period="3mo", interval="1d")

    st.subheader(f"{selected_pair} — Last 3 Months")
    st.line_chart(data["Close"])

    st.write("Latest exchange rate data:")
    st.dataframe(data.tail())

