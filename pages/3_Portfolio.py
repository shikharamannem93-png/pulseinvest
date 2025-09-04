import streamlit as st
from src import simulate_portfolio

st.title('💼 Portfolio Simulation')
budget = st.number_input('Enter your budget ($)', min_value=100, value=1000)

if st.button('Simulate Portfolio'):
    result = simulate_portfolio.simulate(budget)
    st.json(result)
