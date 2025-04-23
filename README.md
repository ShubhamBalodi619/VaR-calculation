# Value at Risk (VaR)- Historical Method

This project implements the **Historical** approach to estimate the Value at Risk (VaR) of an equally weighted multi-asset portfolio using Python.

It leverages actual historical return data to calculate VaR without assuming any specific distribution, providing a non-parametric estimation of potential portfolio losses.

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
- Computes rolling 5-day portfolio returns
- Sorts historical returns to determine empirical quantiles corresponding to different confidence levels
- Estimates VaR directly from the historical distribution of returns

---

## 🔍 Outputs

- Value at Risk (VaR) in both percentage and dollar terms at 99% confidence level.
- Histogram of 5-day portfolio returns with vertical VaR threshold.

---


## 📦 Dependencies

- `numpy`
- `pandas`
- `matplotlib`
- `yfinance`
- `scipy`

You can install the dependencies using:

```bash
pip install numpy pandas matplotlib yfinance scipy
