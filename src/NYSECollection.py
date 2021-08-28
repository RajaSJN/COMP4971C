import numpy as np
import pandas as pd

#Data Source
import yfinance as yf

#Data viz
import plotly.graph_objs as go
# Interval required 5 minutes
#NVDA is the stock data for NVIDIA
data = yf.download(tickers='NVDA', period='5d', interval='1d')
#AMD is the stock data for AMD 
#UBI is the stock price for Ubisoft 
#ATVI is stock name for blizzard
#Print data
data
data.to_csv('src/stock.csv')
print(data)