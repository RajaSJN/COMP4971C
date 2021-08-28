import numpy as np
import pandas as pd

#Data Source
import yfinance as yf

#Data viz
import plotly.graph_objs as go
# Interval required 5 minutes

#.L is used to indicate that the stock is part of the london stock exchange
data = yf.download(tickers='FDEV.L', period='5d', interval='1d')
print(data)