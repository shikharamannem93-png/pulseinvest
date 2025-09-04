import streamlit as st
from src import portfolio_optimization

st.title('📊 Portfolio Analytics')
if st.button('Optimize Portfolio'):
    results = portfolio_optimization.optimize()
    st.json(results)
