# 🧠 Planner Agent
# This agent defines the research workflow for a given stock symbol.

def plan_research(symbol):
    """
    Returns a list of research steps for the given stock symbol.
    """
    return [
        f"Retrieve financial data for {symbol}",
        f"Fetch recent news about {symbol}",
        f"Check macroeconomic indicators",
        f"Download latest SEC filings",
        f"Summarize and evaluate findings"
    ]
