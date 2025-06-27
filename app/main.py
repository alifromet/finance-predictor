import streamlit as st
from app import stocks, indices, forex, options

st.set_page_config(page_title="Finance Dashboard", layout="wide")

tab = st.sidebar.selectbox("Select Market", ["Stocks", "Indices", "Forex", "Options"])

if tab == "Stocks":
    stocks.show()
elif tab == "Indices":
    indices.show()
elif tab == "Forex":
    forex.show()
elif tab == "Options":
    options.show()

