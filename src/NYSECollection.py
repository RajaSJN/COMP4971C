import yfinance as yf
from matplotlib import pyplot as plt
data = yf.download(tickers='BTC-USD',start='2015-01-22', interval='1d')
plt.plot(data['High'])
plt.show()  