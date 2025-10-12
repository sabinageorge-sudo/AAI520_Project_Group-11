# 💼 Multi-Agent Financial Analysis System 

## 🧠 Overview

This project builds an autonomous Investment Research Agent capable of analyzing public companies using financial data, news sentiment, macroeconomic indicators, and regulatory filings. The agent dynamically plans its research steps, routes content to specialized modules, evaluates its own output, and learns across runs.
## 👥 Team Members

| Name        | Role                        | Focus Area                          |
|-------------|-----------------------------|--------------------------------------|
| Senthil Arasu T | Retriever Agent       | Yahoo Finance, earnings, valuation, NewsAPI/Kaggle, prompt chaining    |
| Smita Kasar | Analyser Agent    | Summarizer, Tune summarization parameters, Test the Evaluator–Optimizer loop     |
| Sabina George  | Orchestrator and Memory Agent | Ensure insights are saved, retrieved, and displayed correctly |
## 🧩 Key Features

- **RetrievalQA**: Answers open-domain questions using grounded financial data
- **Prompt Chaining**: Ingest → Preprocess → Classify → Extract → Summarize (for news)
- **Routing**: Directs content to specialized analyzers (e.g., earnings, macro, sentiment)
- **Evaluator–Optimizer**: Evaluates quality of analysis and refines using feedback
- **Memory System**: Stores notes and insights across runs for continuous learning
## 📚 Datasets & APIs Used

- `yfinance` – Stock prices, financial statements
- NewsAPI / Kaggle Financial News – Market sentiment and headlines
- FRED API – Macroeconomic indicators
- SEC EDGAR – Company filings (10-K, 10-Q)
- Alpha Vantage (optional) – Technical indicators and global assets
## 🏗️ Project Structure
<pre>
financial-agent/
├── planner_agent.py         # Plans research steps
├── retriever_agent.py       # Retrieves financials, news, macro, filings
├── analyzer_agent.py        # Summarizes, evaluates, refines insights
├── memory_agent.py          # Stores and retrieves past insights
├── orchestrator.py          # Coordinates the full workflow
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
</pre>
## 🚀 Getting Started

1. Clone the repository  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt

---
3.API Key Setup (.env File)
To securely use external APIs (like NewsAPI, FRED, etc.), create a .env file in the root of your project directory. This file stores your secret keys and keeps them out of your codebase.
4.How to Run the Analysis
Once your .env file is set up and dependencies are installed, you can run the agent from the command line:

## 🚀 Usage

Run the orchestrator with any stock symbol:

```bash
python orchestrator.py AAPL

Replace AAPL with any stock ticker symbol you want to analyze (e.g., TSLA, MSFT, GOOG).

🧠 What Happens:
The planner agent creates a research plan

The retriever agent fetches financials, news, macro data, and filings

The analyzer agent summarizes and evaluates the findings

The memory agent stores the insight for future reference

### 🧪 Evaluation Criteria

- Accuracy and relevance of answers
- Grounding in retrieved financial data or news
- Agent’s ability to reflect and refine its output
- Collaboration across modules and memory usage
## 📅 Milestones

| Week | Goal                                      |
|------|-------------------------------------------|
| 1    | Set up repo, assign roles, load datasets  |
|     | Build retrieval + financial analysis      |
| 2    | Implement news pipeline + routing         |
|     | Add evaluator–optimizer + memory          |
| 3   | Final integration, testing, presentation  |

## 📜 License

This project is for academic and educational purposes only. All datasets and APIs used are publicly available under their respective licenses.

If you reuse or extend this project, please credit the original contributors.
