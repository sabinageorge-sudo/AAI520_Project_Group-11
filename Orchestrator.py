# 🚀 Main Orchestrator
# This agent coordinates all other agents to perform a full analysis.

# Make sure all previous cells (planner, retriever, analyzer, memory) are run first


import sys
from planner_agent import plan_research
from retriever_agent import get_financial_data, get_news, get_macro_data, get_sec_filings
from analyzer_agent import summarize_findings, evaluate_quality, refine_summary
from memory_agent import save_insight, get_insight
def run_analysis(symbol):
        print(f"\n🔎 Starting analysis for {symbol}")
    
        steps = plan_research(symbol)
        print("\n🧭 Planned Steps:")
        for step in steps:
            print(" -", step)
    
        print("\n📊 Retrieving Data...")
        info, financials = get_financial_data(symbol)
        news = get_news(symbol)
        macro = get_macro_data()
        filings = get_sec_filings(symbol)
    
        context = f"""
        Company Info: {info}
        Financials: {financials}
        News Headlines: {[article['title'] for article in news[:2]]}
        Macro Data: {macro}
        Filings: {filings}
        """

        summary = summarize_findings(context, symbol)
        score = evaluate_quality(summary)
    
  
        save_insight(symbol, summary)
    
   
        print("\n📝 Summary:\n", summary)
        print("\n📈 Evaluation:", score)
        print("\n💾 Insight saved for future runs.")
        print("\n🔁 Previous Insight:", get_insight(symbol))

   
if __name__ == "__main__":

        if len(sys.argv) < 2:
            print("Usage: python orchestrator.py <STOCK_SYMBOL>")
        else:
            run_analysis(sys.argv[1])
 