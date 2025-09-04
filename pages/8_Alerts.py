import streamlit as st
from src import alerts

st.title('🔔 Alerts')
if st.button('Send Alerts'):
    alerts.send_alerts()
    st.success('Alerts sent!')
