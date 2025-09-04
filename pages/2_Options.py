import streamlit as st
from src import predict_options

st.title('📈 Options Predictor')
ticker = st.text_input('Enter ticker', 'AAPL')

if st.button('Get Top 5 Options'):
    options_df = predict_options.predict_options(ticker)
    st.dataframe(options_df)
