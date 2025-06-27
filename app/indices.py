import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

def show():
    st.header("📊 Global Market Indices")

    index_map = {
        "S&P 500 (US)": "^GSPC",
        "NASDAQ (US)": "^IXIC",
        "Dow Jones (US)": "^DJI",
        "FTSE 100 (UK)": "^FTSE",
        "DAX (Germany)": "^GDAXI",
        "Nikkei 225 (Japan)": "^N225",
        "CAC 40 (France)": "^FCHI",
        "BSE Sensex (India)": "^BSESN"
    }

    selected_index = st.selectbox("Choose Index", list(index_map.keys()))
    symbol = index_map[selected_index]

    data = yf.Ticker(symbol).history(period="6mo")

    st.subheader(f"{selected_index} — Last 6 Months")
    st.line_chart(data["Close"])

    st.write("Recent data preview:")
    st.dataframe(data.tail())

