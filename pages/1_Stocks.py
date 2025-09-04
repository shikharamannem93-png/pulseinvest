import streamlit as st
import pandas as pd
from src import fetch_data, predict

st.title('📊 Stock Predictions')
tickers = st.text_input('Enter custom tickers (comma separated)', 'AAPL, MSFT, TSLA')

if st.button('Predict Top 5 Stocks'):
    data = fetch_data.get_stock_data(tickers.split(','))
    predictions = predict.predict_stocks(data)
    st.dataframe(predictions)
