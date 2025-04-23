# Value at Risk (VaR) – Monte Carlo Simulation Method

This project implements the **Monte Carlo Simulation** approach to estimate the **Value at Risk (VaR)** of an equally weighted multi-asset portfolio using Python.

It assumes normally distributed returns and uses repeated simulations of portfolio outcomes over a defined time horizon to estimate potential portfolio losses at specified confidence intervals.

---

## 📊 Portfolio Composition

The portfolio consists of the following ETFs:

- **SPY** – S&P 500 ETF  
- **BND** – Total Bond Market ETF  
- **GLD** – Gold ETF  
- **QQQ** – Nasdaq-100 ETF  
- **VTI** – Total Stock Market ETF  

Historical data is fetched via Yahoo Finance using the `yfinance` library.

---

## 📌 Methodology

- Fetches **15 years** of daily closing price data for the portfolio components
- Calculates **daily log returns** and constructs an **equally weighted portfolio**
- Computes the **annualized expected return** and **annualized standard deviation**
- Runs **10,000 Monte Carlo simulations** of 5-day portfolio returns using normally distributed random shocks
- Calculates VaR as the **left-tail percentile** of simulated return distribution

---

## 🔍 Outputs

- **Value at Risk (VaR)** in:
  - **Percentage terms**
  - **Dollar terms** (based on a $1,000,000 portfolio)
- VaR computed at the 99% **confidence level**:
- **Histogram** of 5-day simulated portfolio returns with vertical VaR thresholds

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

