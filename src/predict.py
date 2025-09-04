import pandas as pd

def predict_stocks(data):
    results = []
    for t, df in data.items():
        if not df.empty:
            last_close = df['Close'].iloc[-1]
            results.append({'Ticker': t, 'Score': last_close})
    return pd.DataFrame(results).sort_values('Score', ascending=False).head(5)
