# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 11:28:53 2025

@author: yasse
"""

# Dashboard with equity (SPY), forex (US), commodities (Gold($GC=F), crude oil($WTI, or $USO), wheat($ZW=F)), bonds ($¨TNX)(inflation-linked bonds).
# Data about growth, inflation, volatility, and yield.
# Data goes back as far as possible, with widget slider to choose time frame.

#import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Data Download
def data_download(ticker, filename):
    data=yf.download(ticker,period="max")["Close"]
    data.to_csv(filename)
    return data

data_dict = {}
print(data_dict)
print()
   
ticker_filename={
    "SPY":"spy.csv",
    "DX-Y.NYB":"usd.csv",
    "GC=F":"gold.csv",
    "WTI":"wti.csv",
    "ZW=F":"wheat.csv",
    "^TNX":"bonds.csv"
    }

sanatized_ticker = {ticker:filename.replace('.csv','') for ticker, filename in ticker_filename.items()}


for ticker, filename in ticker_filename.items():
    data_dict[ticker] = data_download(ticker, filename)
    #print(data_dict)
    #print()

print(data_dict.keys())

#Sanity Checks
#Check for missing values
def check_na(data):
    null_sum= data.isna().sum()
    null_percentage=null_sum/len(data)
    print(f"Ratio of missing values : {null_percentage} /n Count of missing values: {null_sum}")

def fill_missing_values(df):
    '''
    Fill missing values using FFILL method, input is the dataframe, and output is the filled dataframe
    '''
    df = df.ffill().dropna()
    return df

def plot_df(ticker):
    data = pd.read_csv(ticker_filename[ticker])
    plt.figure()
    plt.title(sanatized_ticker[ticker])
    plt.plot(data.index, data[ticker])
    plt.savefig(sanatized_ticker[ticker] + '.png')

for ticker in ticker_filename.keys():
    print(f"Checking {ticker}")
    data = pd.read_csv(ticker_filename[ticker], index_col = 0, parse_dates=True)
    check_na(data)
    print()
    data= fill_missing_values(data)
    plot_df(ticker)


spy = pd.read_csv("spy.csv",index_col=0, parse_dates=True)
spy = fill_missing_values(spy)
plot_df('SPY')
print(spy.head())
check_na(spy)