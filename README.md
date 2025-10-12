# 💼 Multi-Agent Financial Analysis System 

## 🧠 Overview

This project builds an autonomous Investment Research Agent capable of analyzing public companies using financial data, news sentiment, macroeconomic indicators, and regulatory filings. The agent dynamically plans its research steps, routes content to specialized modules, evaluates its own output, and learns across runs.
## 👥 Team Members

| Name        | Role                        | Focus Area                          |
|-------------|-----------------------------|--------------------------------------|
| Senthil Arasu T | Planner agent      | Yahoo Finance, earnings, valuation   |
| Smita Kasar | Retriever Agent    | NewsAPI/Kaggle, prompt chaining      |
| Sabina George  | Analyzer Agent | Routing, memory, evaluator–optimizer |
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
investment-research-agent/ │ ├── README.md # Project overview and instructions ├── requirements.txt # Python dependencies ├── data/ # Raw and processed datasets ├── notebooks/ # Exploratory notebooks by team members ├── src/ # Core source code │ ├── agent/ # Planning, routing, evaluation, memory │ ├── pipelines/ # Prompt chaining workflows │ ├── retrievers/ # FAISS or vector DB setup │ └── utils/ # Helpers and configs ├── tests/ # Unit tests and evaluation scripts └── docs/ # Architecture diagrams, team notes
## 🚀 Getting Started

1. Clone the repository  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt

---

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
## 🤝 Contributing

We welcome contributions from all team members! To contribute:

1. Fork the repository
2. Create a new branch: `git checkout -b feature-name`
3. Make your changes and commit: `git commit -m "Add feature"`
4. Push to your branch: `git push origin feature-name`
5. Open a pull request and describe your changes

Please follow consistent naming conventions and comment your code clearly. Use the `/tests` folder to add unit tests for new modules.
## 📜 License

This project is for academic and educational purposes only. All datasets and APIs used are publicly available under their respective licenses.

If you reuse or extend this project, please credit the original contributors.
