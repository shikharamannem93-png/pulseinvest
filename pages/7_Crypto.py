import streamlit as st
from src import crypto_predict

st.title('💰 Crypto Predictions')
if st.button('Predict Crypto'):
    crypto = crypto_predict.predict()
    st.dataframe(crypto)
