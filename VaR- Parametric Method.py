# Importing libraries

import numpy as np
import pandas as pd
import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt
from scipy.stats import norm

# Setting the timeline

years= 15

end_date= dt.datetime.today()
start_date= end_date - dt.timedelta(days=years*365)
print(start_date)
print(end_date)

# Creating a list of tickers

tickers= ["SPY", "BND", "GLD", "QQQ", "VTI"]

# Downloading the daily close prices for the tickers

close_df= pd.DataFrame()

for ticker in tickers:
    data= yf.download(ticker, start= start_date, end= end_date)
    close_df[ticker]= data["Close"]

print(close_df.head())

# Calculating the daily log returns and drop any NAs

log_returns= np.log(close_df/close_df.shift(1))
log_returns= log_returns.dropna()

print(log_returns.head())

# Creating an equally weighted portfolio

portfolio_value= 1000000

weights= np.array([1/len(tickers)]*len(tickers))
print(weights)

# Calculating the historical portfolio returns

historical_returns= (log_returns * weights).sum(axis=1)
print(historical_returns.head())

# Finding the X-day historical returns

days= 5

returns_range= historical_returns.rolling(window= days).sum()
returns_range= returns_range.dropna()
print(returns_range.head())

# Creating a covariance matrix for the securities

cov_matrix= log_returns.cov() * 252

print(cov_matrix)

# Calculating portfolio std. dev.

portfolio_std_dev= np.sqrt(weights.T @ cov_matrix @ weights)

print(portfolio_std_dev)

# Setting different confidence levels to visualize

confidence_levels= [0.9, 0.95, 0.99, 0.999]

# Calculating VaRs at different levels

VaRs_percentage= []
VaRs_dollars= []

for i in confidence_levels:
    VaR= historical_returns.mean() * days - norm.ppf(i) * portfolio_std_dev * np.sqrt(days/252)
    VaRs_percentage.append(VaR)
    VaRs_dollars.append(VaR * portfolio_value)

print("Confidence Level(%)       Value at Risk(%)       Value at Risk($)")

for i in range(0,len(confidence_levels)):
    print(f"        {confidence_levels[i]*100}%                 {(VaRs_percentage[i]*100).round(2)}%                ${(VaRs_dollars[i]).round(2)}")

# Plotting the results of historical returns

returns_range_percent= returns_range * 100
# print(returns_range_percent.head())

plt.figure(figsize=(10,6))
plt.hist(returns_range, bins=100, color="lightblue")
plt.title(f"Distribution of Portfolio {days}-day Returns")
plt.xlabel(f"{days}-day Portfolio returns")
plt.ylabel("Frequency")

colors= ["red", "yellow", "purple", "black"]

for i in range(0,len(confidence_levels)):
    plt.axvline(VaRs_percentage[i], color= colors[i], linestyle= "--", linewidth= 2, label= f"VaR at {confidence_levels[i]}% confidence level")

plt.legend(loc= "upper left")

plt.show()
