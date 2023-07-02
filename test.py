# import yfinance as yf
# import pandas as pd
# import streamlit as st
# # st.write("""
# # # Simple Stock Price App

# # Shown are the stock closing price and volume of Google!

# # """)

# tickerSymbol = 'GOOGL'
# # get data on this ticker
# tickerData = yf.ticker(tickerSymbol)
# # get the historical prices for this ticker
# tickerDf = tickerData.history(period = '1d', start = '2010-05-31', end = '2021-05-31')
# # open High   Low Close  Volume  Dividends  Stock  Splits

# st.line_chart(tickerDf.Close)
# st.line_chart(tickerDf.Volume)

import yfinance as yf

msft = yf.Ticker("MSFT")

# get all stock info
msft.info

# get historical market data
hist = msft.history(period="1mo")
print(hist)

# Markdown Cheat Sheet