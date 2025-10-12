
# 🔍 Retriever Agent
# This agent fetches financial data, news, macro indicators, and SEC filings.

import yfinance as yf
from newsapi import NewsApiClient
from fredapi import Fred
from sec_edgar_downloader import Downloader

from dotenv import load_dotenv
import os

load_dotenv()
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")
FRED_API_KEY = os.getenv("FRED_API_KEY")

def get_financial_data(symbol):
    stock = yf.Ticker(symbol)
    return stock.info, stock.financials

def get_news(symbol):   
    print(f"🔎 Fetching news for {symbol}...")
    newsapi = NewsApiClient(api_key=NEWSAPI_KEY)
    try:
        articles = newsapi.get_everything(q=symbol, language='en', sort_by='publishedAt', page_size=5)
        print(f"📄 Retrieved {len(articles['articles'])} articles.")
        return articles['articles']
    except Exception as e:
        print(f"❌ Error fetching news: {e}")
        return []

def get_macro_data():
    fred = Fred(api_key=FRED_API_KEY)
    return {
        "interest_rate": fred.get_series('FEDFUNDS').tail(1).values[0],
        "inflation": fred.get_series('CPALTT01USM657N').tail(1).values[0]
    }

def get_sec_filings(symbol):
    downloader = Downloader(company_name="MultiAgentFinanceTeam", email_address="sabinageorge@sandiego.edu")
    downloader.get("10-K", symbol)
    return f"Downloaded 10-K filings for {symbol}"