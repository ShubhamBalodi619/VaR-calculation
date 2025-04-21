# Value at Risk (VaR)- Parametric Method

This project implements the **Parametric (Variance-Covariance)** approach to estimate the Value at Risk (VaR) of an equally weighted multi-asset portfolio using Python.

It assumes normally distributed returns and calculates VaR analytically based on portfolio volatility, return distributions, and confidence intervals.

---

## 📊 Portfolio Composition

The portfolio consists of the following ETFs:

- **SPY** – S&P 500 ETF
- **BND** – Total Bond Market ETF
- **GLD** – Gold ETF
- **QQQ** – Nasdaq-100 ETF
- **VTI** – Total Stock Market ETF

Data is fetched via Yahoo Finance using `yfinance`.

---

## 📌 Methodology

- Fetches 15 years of daily price data
- Calculates daily log returns and constructs an equally weighted portfolio
- Computes annualized covariance matrix of asset returns
- Derives portfolio standard deviation
- Calculates VaR using the formula:

\[
\text{VaR} = \mu \cdot T - z_{\alpha} \cdot \sigma \cdot \sqrt{\frac{T}{252}}
\]

Where:
- \( \mu \) = portfolio mean daily return  
- \( \sigma \) = portfolio standard deviation  
- \( T \) = time horizon (5 days)  
- \( z_{\alpha} \) = z-score at given confidence level

---

## 🔍 Outputs

- Value at Risk (VaR) in both percentage and dollar terms at different confidence levels:
  - 90%
  - 95%
  - 99%
  - 99.9%
- Histogram of 5-day portfolio returns with vertical VaR thresholds

---
