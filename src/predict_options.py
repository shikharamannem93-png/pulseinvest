import pandas as pd

def predict_options(ticker):
    data = [
        {'Option': f'{ticker} Call 200', 'Delta': 0.6, 'Score': 0.85},
        {'Option': f'{ticker} Put 180', 'Delta': -0.4, 'Score': 0.75},
    ]
    return pd.DataFrame(data).head(5)
