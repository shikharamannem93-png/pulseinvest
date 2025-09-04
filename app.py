import streamlit as st

st.set_page_config(page_title='Stock & Options Predictor', layout='wide')

st.title('📈 Stock & Options Predictor App')
st.sidebar.success('Select a page above.')

st.markdown('''
Welcome to the **Stock & Options Predictor App**.  
Use the sidebar to navigate through the app's features:
- Stocks, Options, Portfolio, Backtesting
- Analytics, Sentiment, Crypto, Alerts, Settings
''')
