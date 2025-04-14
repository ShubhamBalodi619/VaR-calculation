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
# print(start_date)
# print(end_date)

# Creating a list of tickers
tickers= ["SPY", "BND", "GLD", "QQQ", "VTI"]

# Downloading the daily close prices for the tickers
close_df= pd.DataFrame()

for ticker in tickers:
    data= yf.download(ticker, start= start_date, end= end_date)
    close_df[ticker]= data["Close"]

close_df= close_df.dropna()
print(close_df.head())

# Calculating the daily log returns and drop any NAs
log_returns= np.log(close_df/close_df.shift(1))
log_returns= log_returns.dropna()

print(log_returns.head())

# Creating an equally weighted portfolio
portfolio_value= 1000000

weights= np.array([1/len(tickers)]*len(tickers))

# print(weights)

# Calculating the historical portfolio returns
historical_returns= (log_returns * weights).sum(axis=1)
print(historical_returns.head())

# Finding the X-day historical returns
days= 5

returns_range= historical_returns.rolling(window= days).sum()
returns_range= returns_range.dropna()
print(returns_range.head())

#Specifying a confidence interval and calculating VaR using the historical method
confidence_interval= 0.99

VaR_percentage= np.percentile(returns_range, 100 - (confidence_interval * 100))
VaR_dollar= (VaR_percentage * portfolio_value) * -1

print(f"VaR= {VaR_percentage*-100}%")
print(f"VaR= ${VaR_dollar}")

# Plotting the results of historical returns
returns_range_percent= returns_range * 100
# print(returns_range_percent.head())

plt.figure(figsize=(10,6))
plt.hist(returns_range, bins=100, color="lightblue")
plt.title(f"Distribution of Portfolio {days}-day Returns")
plt.xlabel(f"{days}-day Portfolio returns")
plt.ylabel("Frequency")
plt.axvline(VaR_percentage, color= "red", linestyle= "--", linewidth= 2, label= f"VaR at {confidence_interval}% confidence level")
plt.legend(loc= "upper left")

plt.show()

