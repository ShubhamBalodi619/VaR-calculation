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

# Creating a function used to calculate portfolio expected return
def expected_return(weights, log_returns):
    return np.sum(log_returns.mean() * weights * 252)

# Creating a function to calculate the portfolio std. dev.
def std_dev(weights, cov_matrix):
    return np.sqrt(weights.T @ cov_matrix @ weights)

# Creating a covariance matrix for the securities
cov_matrix= log_returns.cov() * 252

# Creating an equally weighted portfolio and finding the total portfolio expected return and std. dev.
portfolio_value= 1000000

weights= np.array([1/len(tickers)]*len(tickers))
portfolio_expected_return= expected_return(weights, log_returns)
portfolio_std_dev= std_dev(weights, cov_matrix)

# Creating a function that gives a random Z-score based on a normal distribution
def random_z_score():
    return np.random.normal(0,1)

# Creating a function to calculate scenario gain/loss
days= 5

def scenario_gain_loss(portfolio_expected_return, portfolio_std_dev, z_score, days):
    return portfolio_expected_return * days/252 - z_score * portfolio_std_dev * np.sqrt(days/252)

# Running 10,000 simulations
simulations= 10000
scenario_returns=[]

for i in range(simulations):
    z_score= random_z_score()
    scenario_returns.append(scenario_gain_loss(portfolio_expected_return, portfolio_std_dev, z_score, days))

# Specifying a confidence interval & calculating the VaR
confidence_level= 0.99

VaR_percent= np.percentile(scenario_returns, 100 * (1 - confidence_level))
VaR_dollar= (VaR_percent * portfolio_value) * -1

print(f"VaR= {(VaR_percent*-100).round(2)}%")
print(f"VaR= ${VaR_dollar.round(2)}")

# Plotting the result of all 10,000 simulations
plt.figure(figsize=(10,6))
plt.hist(scenario_returns, bins=100, color="lightblue")
plt.title(f"Distribution of Portfolio Gain/Loss over {days} days")
plt.xlabel("Scenario Gain/Loss")
plt.ylabel("Frequency")
plt.axvline(VaR_percent, color= "red", linestyle= "--", linewidth= 2, label= f"VaR at {confidence_level}% confidence level")
plt.legend(loc= "upper left")

plt.show()
