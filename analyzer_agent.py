import pandas as pd

def analyze_data(retrieved):
    """
    Analyze financial data and calculate price trends.
    """
    financial_data = retrieved.get("financial_data", {})
    info = financial_data.get("info", {})
    company_name = info.get("longName", "Unknown Company")

    # Price trend analysis
    hist_prices = financial_data.get("hist_prices", None)
    trend_info = {}
    if hist_prices is not None and not hist_prices.empty:
        start_price = hist_prices["Close"].iloc[0]
        end_price = hist_prices["Close"].iloc[-1]
        pct_change = ((end_price - start_price) / start_price) * 100
        trend_info = {
            "trend": "Uptrend" if pct_change > 0 else "Downtrend",
            "price_change_%": round(pct_change, 2),
            "start_price": float(start_price),
            "end_price": float(end_price)
        }
    else:
        trend_info = {"trend": "N/A", "price_change_%": "N/A", "start_price": "N/A", "end_price": "N/A"}

    # Key metrics
    metrics = {
        "marketCap": info.get("marketCap"),
        "beta": info.get("beta"),
        "trailingPE": info.get("trailingPE"),
        "forwardPE": info.get("forwardPE"),
        "eps": info.get("trailingEps"),
        "dividendYield": info.get("dividendYield")
    }

    insights = {
        "company": company_name,
        **metrics,
        **trend_info
    }

    return insights
