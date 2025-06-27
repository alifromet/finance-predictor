import streamlit as st
import yfinance as yf

def show():
    st.header("Stock Market")
    symbol = st.text_input("Enter Stock Symbol", "AAPL")
    ticker = yf.Ticker(symbol)
    hist = ticker.history(period="6mo")
    st.line_chart(hist["Close"])

