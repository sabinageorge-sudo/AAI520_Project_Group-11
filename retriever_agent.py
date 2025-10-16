import yfinance as yf

def retrieve_all_data(ticker):
    """
    Retrieve financial info and historical prices for a given ticker.
    Ensures at least 1 year of daily data for trend analysis.
    """
    stock = yf.Ticker(ticker)

    # Company info
    info = stock.info

    # Historical prices (1 year)
    hist_prices = stock.history(period="1y", interval="1d")
    
    # If empty, try 2 years as fallback
    if hist_prices.empty:
        hist_prices = stock.history(period="2y", interval="1d")
    
    return {
        "financial_data": {
            "info": info,
            "hist_prices": hist_prices
        }
    }
