import pandas as pd
import numpy as np

def run_backtest():
    dates = pd.date_range('2023-01-01', periods=200)
    portfolio = np.cumsum(np.random.randn(200)) + 100
    return pd.DataFrame({'Portfolio': portfolio}, index=dates)
