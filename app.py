import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

# Page setup
st.set_page_config(page_title="Stock & Options Predictor", layout="wide")

st.title("🏠 Home Dashboard – Stock & Options Predictor")

# Sidebar navigation hint
st.sidebar.success("⬅️ Use the sidebar to explore pages")

# --- Market Overview Section ---
st.subheader("📊 Market Overview")
col1, col2, col3 = st.columns(3)

# Fetch live index data
def get_index_data(ticker):
    data = yf.download(ticker, period="5d", interval="1d")
    last = data["Close"].iloc[-1]
    change = (last - data["Close"].iloc[-2]) / data["Close"].iloc[-2] * 100
    return last, change

sp500, sp500_chg = get_index_data("^GSPC")
nasdaq, nasdaq_chg = get_index_data("^IXIC")
dow, dow_chg = get_index_data("^DJI")

col1.metric("S&P 500", f"{sp500:.2f}", f"{sp500_chg:.2f}%")
col2.metric("NASDAQ", f"{nasdaq:.2f}", f"{nasdaq_chg:.2f}%")
col3.metric("Dow Jones", f"{dow:.2f}", f"{dow_chg:.2f}%")

# --- Predictions Snapshot ---
st.subheader("🔮 Today’s Top Predictions")

sample_stocks = pd.DataFrame({
    "Ticker": ["AAPL", "MSFT", "TSLA", "GOOGL", "NVDA"],
    "Score": [0.91, 0.88, 0.86, 0.82, 0.80]
})

sample_options = pd.DataFrame({
    "Option": ["AAPL Call 200", "TSLA Put 250", "MSFT Call 350", "GOOGL Put 120", "NVDA Call 500"],
    "Risk-Score": [0.85, 0.77, 0.82, 0.75, 0.80]
})

col4, col5 = st.columns(2)
with col4:
    st.write("📈 Top 5 Stocks")
    st.dataframe(sample_stocks)

with col5:
    st.write("📊 Top 5 Options")
    st.dataframe(sample_options)

# --- Watchlist ---
st.subheader("👀 Your Watchlist")
watchlist = st.text_input("Enter tickers (comma separated)", "AAPL, MSFT, TSLA")
if st.button("Update Watchlist"):
    tickers = [t.strip() for t in watchlist.split(",")]
    st.success(f"✅ Watchlist updated: {', '.join(tickers)}")

# --- Portfolio Preview ---
st.subheader("💼 Portfolio Snapshot")
portfolio_value = 12500
profit_today = +2.4
st.metric("Portfolio Value", f"${portfolio_value:,}", f"{profit_today}%")

# --- Quick Navigation ---
st.subheader("🚀 Quick Actions")
col6, col7, col8, col9 = st.columns(4)
with col6:
    if st.button("📊 Stocks"):
        st.switch_page("pages/1_Stocks.py")
with col7:
    if st.button("📈 Options"):
        st.switch_page("pages/2_Options.py")
with col8:
    if st.button("💼 Portfolio"):
        st.switch_page("pages/3_Portfolio.py")
with col9:
    if st.button("📰 Sentiment"):
        st.switch_page("pages/6_Sentiment.py")