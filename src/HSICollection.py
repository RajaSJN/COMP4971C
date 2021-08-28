import numpy as np
import pandas as pd

#Data Source
import yfinance as yf

#Data viz
import plotly.graph_objs as go
# Interval required 5 minutes
#.HK is used to indicate the stock is part of the HANG SENG INDEX
data = yf.download(tickers='3067.HK', period='5d', interval='1d')
print(data)