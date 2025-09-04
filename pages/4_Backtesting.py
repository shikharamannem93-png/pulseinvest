import streamlit as st
from src import backtesting

st.title('📉 Backtesting')
if st.button('Run Backtest'):
    results = backtesting.run_backtest()
    st.line_chart(results)
