"""
orchestrator.py
Coordinates the workflow using Yahoo Finance data and prints formatted insights.
"""

from planner_agent import PlannerAgent
from retriever_agent import RetrieverAgent
from analyzer_agent import AnalyzerAgent
from memory_agent import MemoryAgent

def print_insights_summary(insights):
    """Print a readable summary of insights"""
    print("\n=== Price Trend ===")
    pt = insights['price_trend']
    print(f"Trend: {pt['trend']}, Change: {pt['percentage_change']}%")
    print(f"Start: {pt['start_price']} on {pt['start_date']}")
    print(f"End: {pt['end_price']} on {pt['end_date']}")

    print("\n=== Key Metrics ===")
    for k, v in insights['key_metrics'].items():
        print(f"{k}: {v}")

    print("\n=== Recent Financial Summary ===")
    fs = insights['financial_summary']
    for section, data in fs.items():
        print(f"\n[{section}]")
        # Show last 3 periods
        for period, metrics in list(data.items())[:3]:
            print(f"{period}:")
            for metric, value in metrics.items():
                print(f"    {metric}: {value}")

def main():
    companies = ["AAPL", "MSFT", "TSLA"]

    # Initialize agents
    planner = PlannerAgent()
    retriever = RetrieverAgent()
    analyzer = AnalyzerAgent()
    memory = MemoryAgent()

    # Generate research plan
    research_plan = planner.plan_research(companies)

    for company, tasks in research_plan.items():
        print(f"\n--- Researching {company} ---")

        # Retrieve data
        financials = retriever.get_financials(company)
        hist_prices = retriever.get_historical_prices(company)
        key_metrics = retriever.get_key_metrics(company)

        # Analyze data
        financial_summary = analyzer.summarize_financials(financials)
        price_trend = analyzer.analyze_price_trends(hist_prices)
        insights = analyzer.refine_insights(financial_summary, price_trend, key_metrics)

        # Store insights
        memory.store_insights(company, insights)

        # Print formatted insights
        print(f"\nInsights for {company}:")
        print_insights_summary(insights)

if __name__ == "__main__":
    main()
