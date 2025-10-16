from retriever_agent import retrieve_all_data
from analyzer_agent import analyze_data
from memory_agent import MemoryAgent  # ensure this exists
from datetime import datetime

def print_insights(insights):
    """
    Nicely format and print company insights.
    """
    print(f"\n📈 Insights for {insights.get('company', 'Unknown')}:")
    print("-" * 50)

    # Metrics
    for key in ["marketCap", "beta", "trailingPE", "forwardPE", "eps", "dividendYield"]:
        value = insights.get(key, "N/A")
        if isinstance(value, float):
            value = round(value, 2)
        print(f"{key}: {value}")

    # Price trend
    print(f"\nTrend: {insights.get('trend', 'N/A')}")
    print(f"Price change (%): {insights.get('price_change_%', 'N/A')}")
    print(f"Start price: {insights.get('start_price', 'N/A')}")
    print(f"End price: {insights.get('end_price', 'N/A')}")

    # Timestamp
    print(f"\nTimestamp: {datetime.now().isoformat()}")
    print("=" * 50)

def main():
    tickers = ["AAPL", "MSFT", "TSLA"]
    memory = MemoryAgent()  # initialize memory

    for ticker in tickers:
        print(f"\n--- Researching {ticker} ---")
        retrieved = retrieve_all_data(ticker)
        insights = analyze_data(retrieved)
        memory.store_insights(ticker, insights)
        print_insights(insights)

if __name__ == "__main__":
    main()
