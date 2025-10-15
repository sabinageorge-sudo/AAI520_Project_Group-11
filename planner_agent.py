"""
planner_agent.py
Plans research steps for the autonomous investment research agent.
"""

class PlannerAgent:
    def __init__(self):
        pass

    def plan_research(self, company_list):
        plan = {}
        for company in company_list:
            plan[company] = [
                "Retrieve financial data from Yahoo Finance",
                "Retrieve historical stock prices",
                "Analyze key metrics (P/E, EPS, Revenue)",
                "Summarize insights"
            ]
        return plan

# Example usage
if __name__ == "__main__":
    planner = PlannerAgent()
    companies = ["AAPL", "MSFT", "TSLA"]
    plan = planner.plan_research(companies)
    print(plan)
