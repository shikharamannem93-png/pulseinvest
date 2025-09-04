import yfinance as yf
import pandas as pd

def get_stock_data(tickers):
    data = {}
    for t in tickers:
        ticker = yf.Ticker(t.strip())
        hist = ticker.history(period='1y')
        data[t] = hist
    return data
