import streamlit as st
import yfinance as yf

def show():
    st.header("📈 Options Chain Viewer")

    symbol = st.text_input("Enter Stock Symbol (e.g., AAPL, MSFT, TSLA)", "AAPL")
    ticker = yf.Ticker(symbol)

    try:
        options_dates = ticker.options
        if not options_dates:
            st.warning("No options data available for this symbol.")
            return

        selected_date = st.selectbox("Select Expiry Date", options_dates)

        chain = ticker.option_chain(selected_date)

        st.subheader(f"Calls - Expiry: {selected_date}")
        st.dataframe(chain.calls)

        st.subheader(f"Puts - Expiry: {selected_date}")
        st.dataframe(chain.puts)

    except Exception as e:
        st.error(f"Failed to fetch options data: {e}")

