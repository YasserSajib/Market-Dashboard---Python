# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 11:47:29 2025

@author: yasse
"""

#1 Import libraries

import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import streamlit as st


#2 function definition

#3 download the data

def download_data(tickers, start_date = None, end_date = None):
    
    data = yf.download(
        tickers, 
        start_date , 
        end_date, 
        auto_adjust = True, #auto_adjust sert à ajuster le prix (ex: stock split, dividendes...)
        progress = False
        )['Close']

    return data

#4 save the data locally

#5 load the data
def load_data(file) :
    data = pd.read_csv(file, index_col = 0, parse_dates = True)
    return data

#6 prepocess the data
def preprocess(data):
    data = data.ffill().dropna()
    return(data)

def normalize(prices):
    returns = prices.pct_change()
    cum_returns = (1+ returns).cumprod()
    return cum_returns

def plot(data, title):
    fig = plt.figure(figsize =(8.6))
    plt.plot(data)
    plt.title(title)
    plt.xticks(rotation = 45)
    plt.show()
    return fig

#7 Create Dashboard
def create_dashboard(data, title,fig): 
    st.title(title)
    st.pyplot(fig)
    


#8 Main workflow (function call)

#9 download the data
tickers =["ES=F", "ZN=F", "GC=F", "CL=F", "DX=F", "ZW=F"]
data = download_data (tickers, start_date = None, end_date = None)
print(data)

#10 save the data locally
data.to_csv("data.csv")

#11 load the data
prices = load_data("data.csv")
print(prices)

#12 prepocess the data
prices = preprocess(prices)
cum_returns = normalize(prices)
print(cum_returns)

cum_returns.plot()
plt.show()

title = "Cross-Asset Money Monitor"
fig = plot(cum_returns, title)
create_dashboard(cum_returns, title, fig)
