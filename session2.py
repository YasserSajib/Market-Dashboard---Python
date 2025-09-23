# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 22:42:35 2025

@author: yasse
"""

# Lest's create a Market Dashboard that gives data of different assets classes.
# The asset classes : Equity, FX, Commodities and bonds.
# Let's define the proxies
# Equity:SPY ; FX:USD Index ; Commodities: Gold, Crued Oil, Wheat, Bonds:tresuries
 
# Import packages
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Let's import daily data of SPY
#data = yf.download("SPY", start = '2000-01-01', end = '2025-09-23')['Close']
#data.to_csv("SPY_data.csv")
#print(data.index)

spy = (pd.read_csv("spy_data.csv", index_col=0 , parse_dates = True)['SPY'].pct_change() + 1 ).cumprod() 


# Let's check if there is any missing values
#missing_calues = data.isnull().sum() 


# Now we will plot the data
spy.plot(label='SPY')
plt.ylabel("Price in $")
plt.title("SPY")
plt.yscale('log')


# Let's import data for FX using USD Index
usd = (yf.download("DX-Y.NYB", start = spy.index.min())['Close'].pct_change() + 1).cumprod()
usd["DX-Y.NYB"].plot(label = 'USD Index')

plt.legend()
plt.show()