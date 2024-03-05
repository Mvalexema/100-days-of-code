import datetime
import numpy as np
import pandas as pd
import yfinance as yf
import digifi as dgf
import plotly.express as px

tickers = ["AAPL", "AMD", "NVDA"]
start_date = datetime.datetime(2015, 1, 1)
end_date = datetime.datetime.today()

# company = yf.Ticker("AAPL")
# print(company.info)
# print(company.financials)

data: pd.DataFrame = yf.download(tickers, start=start_date, end=end_date)["Adj Close"]

assets = dict()
predictable_income = dict()
for ticker in data.columns:
    assets[ticker] = data[ticker].to_numpy()
    predictable_income[ticker] = np.zeros(len(data[ticker]))

portfolio = dgf.Portfolio(assets=assets, weights=np.array([0.5, 0.25, 0.25]), predictable_income=predictable_income)
print(portfolio.maximize_sharpe_ratio(r=0.04))
result = portfolio.efficient_frontier(r=0.04)

x = result["eff"]["std"]
y = result["eff"]["return"]
fig = px.line(x=x, y=y)
fig.show()
