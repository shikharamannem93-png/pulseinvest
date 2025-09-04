import streamlit as st
from src import sentiment_analysis

st.title('📰 Market Sentiment')
if st.button('Analyze Sentiment'):
    sentiment = sentiment_analysis.get_sentiment('AAPL')
    st.json(sentiment)
