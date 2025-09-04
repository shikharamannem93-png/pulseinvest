import pandas as pd

def predict():
    data = [
        {'Crypto': 'BTC', 'Prediction': 'Bullish'},
        {'Crypto': 'ETH', 'Prediction': 'Neutral'},
    ]
    return pd.DataFrame(data)
