"""
analyzer_agent.py
Summarizes, evaluates, and refines insights from Yahoo Finance data.
"""

import pandas as pd

class AnalyzerAgent:
    def __init__(self):
        pass

    def summarize_financials(self, financials):
        """
        Summarize income statement, balance sheet, and cash flow
        """
        summary = {}
        for key, df in financials.items():
            if isinstance(df, pd.DataFrame):
                # Convert Timestamps/columns to strings
                df_copy = df.copy()
                df_copy.columns = [str(c) for c in df_copy.columns]
                summary[key] = df_copy.head(3).to_dict()
        return summary

    def analyze_price_trends(self, hist_prices):
        """
        Simple trend analysis using closing prices
        """
        if hist_prices.empty:
            return "No historical data"

        # Use .iloc to access first/last rows (avoids FutureWarning)
        start_price = hist_prices['Close'].iloc[0]
        end_price = hist_prices['Close'].iloc[-1]
        change = ((end_price - start_price) / start_price) * 100
        trend = "Uptrend" if change > 0 else "Downtrend" if change < 0 else "Flat"

        # Convert index Timestamps to strings for JSON
        hist_prices_index = [str(i) for i in hist_prices.index]

        return {
            "trend": trend,
            "percentage_change": round(change, 2),
            "start_date": hist_prices_index[0],
            "end_date": hist_prices_index[-1],
            "start_price": float(start_price),
            "end_price": float(end_price)
        }

    def refine_insights(self, financial_summary, price_trend, key_metrics):
        """
        Combine all insights into a dictionary and convert any non-serializable objects to strings
        """
        def convert(obj):
            if isinstance(obj, pd.Timestamp):
                return str(obj)
            elif isinstance(obj, dict):
                return {convert(k): convert(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [convert(i) for i in obj]
            elif isinstance(obj, pd.Series):
                return obj.to_dict()
            else:
                return obj

        insights = {
            "financial_summary": convert(financial_summary),
            "price_trend": convert(price_trend),
            "key_metrics": convert(key_metrics)
        }
        return insights


# Example usage
if __name__ == "__main__":
    import retriever_agent as ra
    retriever = ra.RetrieverAgent()
    analyzer = AnalyzerAgent()

    # Retrieve sample data
    financials = retriever.get_financials("AAPL")
    hist_prices = retriever.get_historical_prices("AAPL")
    key_metrics = retriever.get_key_metrics("AAPL")

    financial_summary = analyzer.summarize_financials(financials)
    price_trend = analyzer.analyze_price_trends(hist_prices)
    insights = analyzer.refine_insights(financial_summary, price_trend, key_metrics)

    print(insights)
