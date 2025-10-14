"""
retriever_agent.py
Retrieves financial data and historical stock prices from Yahoo Finance.
"""

import yfinance as yf
import pandas as pd

class RetrieverAgent:
    def __init__(self):
        pass

    def get_financials(self, ticker):
        """Retrieve income statement, balance sheet, cash flow"""
        data = yf.Ticker(ticker)
        financials = {
            "income_statement": data.financials,
            "balance_sheet": data.balance_sheet,
            "cash_flow": data.cashflow
        }
        return financials

    def get_historical_prices(self, ticker, period="1y"):
        """
        Retrieve historical stock prices for the given period.
        period: '1y', '6mo', '1mo', etc.
        """
        data = yf.Ticker(ticker)
        hist = data.history(period=period)
        return hist

    def get_key_metrics(self, ticker):
        """Retrieve key metrics like P/E, EPS, market cap"""
        data = yf.Ticker(ticker)
        info = data.info
        metrics = {
            "marketCap": info.get("marketCap"),
            "trailingPE": info.get("trailingPE"),
            "forwardPE": info.get("forwardPE"),
            "eps": info.get("trailingEps"),
            "beta": info.get("beta"),
            "dividendYield": info.get("dividendYield")
        }
        return metrics


# Example usage
if __name__ == "__main__":
    retriever = RetrieverAgent()
    print(retriever.get_financials("AAPL"))
    print(retriever.get_historical_prices("AAPL").head())
    print(retriever.get_key_metrics("AAPL"))
