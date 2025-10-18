# 💼 Multi-Agent Financial Analysis System 

## 🧠 Overview

This project builds an autonomous Investment Research Agent capable of analyzing public companies using financial data, news sentiment, macroeconomic indicators, and regulatory filings. The agent dynamically plans its research steps, routes content to specialized modules, evaluates its own output, and learns across runs.
## 👥 Team Members

| Name        | Role                        | Focus Area                          |
|-------------|-----------------------------|--------------------------------------|
| Senthil Arasu T | Retriever Agent       | Yahoo Finance, earnings, valuation, NewsAPI/Kaggle, prompt chaining    |
| Smita Kasar | Analyser Agent    | Summarizer, Tune summarization parameters, Test the Evaluator–Optimizer loop     |
| Sabina George  | Reporter Agent | Ensure insights are saved, retrieved, and displayed correctly |
## 🧩 Key Features

- **RetrievalQA**: Answers open-domain questions using grounded financial data
- **Prompt Chaining**: Ingest → Preprocess → Classify → Extract → Summarize (for news)
- **Routing**: Directs content to specialized analyzers (e.g., earnings, macro, sentiment)
- **Evaluator–Optimizer**: Evaluates quality of analysis and refines using feedback
## 📚 Datasets & APIs Used

- `yfinance` – Stock prices, financial statements
- NewsAPI / Kaggle Financial News – Market sentiment and headlines
- FRED API – Macroeconomic indicators
- SEC EDGAR – Company filings (10-K, 10-Q)
- Alpha Vantage (optional) – Technical indicators and global assets
## 📌 Project Overview
The system simulates a team of three AI agents:

News Analyst: Summarizes recent financial news using NewsAPI and vector embeddings.

Financial Analyst: Interprets market signals, economic indicators, and company data.

Reporter: Synthesizes insights into a coherent market briefing.

Agents communicate and collaborate using LangChain’s tool-calling framework and OpenAI’s GPT models.

## 🚀 Getting Started in Google Colab 

### Step 1: Clone the repository
```bash
!rm -rf AAI520_Project_Group-11
!git clone https://github.com/sabinageorge-sudo/AAI520_Project_Group-11.git
%cd AAI520_Project_Group-11

```
 
### 2. Set Up the Environment
```bash
!pip install transformers torch yfinance newsapi-python fredapi sec-edgar-downloader \
python-dotenv requests langchain langchain-core langchain-community \
langchain-huggingface langchain-openai faiss-cpu tiktoken
```
--- 
### 3. Configure API Keys  
 
Create a .env file in the root directory with the following content
```bash
import os
os.environ["OPENAI_API_KEY"] = "your_openai_api_key"
os.environ["NEWS_API_KEY"] = "your_newsapi_key"
os.environ["FRED_API_KEY"] = "your_fredapi_key"

```
💡 You can also use a .env file and load it with dotenv if preferred.
```   
✅ These keys are required to fetch news and macroeconomic data.
```
---
### 5. Usage:
After setup, run the main script:
--- 
```bash
  !python multiagent_finanacialanalysis_aai520_final.py
```
 
Replace AAPL with any stock ticker symbol you want to analyze (e.g., TSLA, MSFT, GOOG). This will trigger the full agent workflow: planning, retrieving data, analyzing insights, and saving the result.

## 🧭 What Happens Next
✅ The system initializes all agents and tools.

📅 It generates a Daily Market Briefing based on recent financial news.

🧾 Then, it prompts you to:

Enter a stock ticker (e.g., AAPL, TSLA)

Enter the company name (e.g., Apple, Tesla)

📈 The agents analyze the company’s financials, filings, and market context.

🧠 A detailed company-specific financial report is generated.

### 🧪 Evaluation Criteria

- Accuracy and relevance of answers
- Grounding in retrieved financial data or news
- Agent’s ability to reflect and refine its output
- Collaboration across modules and memory usage

## 📂 File Structure

```text
AAI520_Project_Group-11/
├── multiagent_finanacialanalysis_aai520_final.py  # Main script
├── README.md                                      # This file
├── requirements                                   # Dependency list
```
## 🧠 Technologies Used
LangChain: Agent orchestration and tool calling

OpenAI GPT-3.5/GPT-4: LLMs for reasoning and generation

SentenceTransformers: Embedding financial news

FAISS: Vector store for semantic search

NewsAPI, FRED, SEC-EDGAR: Real-time financial data sources

## ⚠️ Notes
If API keys are missing or invalid, the system will fall back to dummy data.

TensorFlow warnings in Colab are safe to ignore.

GPU is not required but can be enabled for faster embedding.
inancial news.

## 📈 Sample Output

######################################################################
### Comprehensive Company Analysis Workflow for 'Cisco' Completed ###
######################################################################


======================================================================
          FINAL COMPREHENSIVE REPORT FOR CISCO           
======================================================================
## Executive Summary
This financial report provides a comprehensive analysis of Cisco Systems, Inc. (CSCO) based on recent news, stock performance, macroeconomic context, and investment outlook. Cisco operates in the technology sector and faces influences from semiconductor advancements, supply chain disruptions, and market dynamics. The company's stock data shows a positive trend over the past year, with a current price of $70.13. Macroeconomic data indicates a gradual increase in the Consumer Price Index (CPI). The investment outlook suggests holding positions with a focus on monitoring industry trends and external factors.

## Recent News Highlights
1. The semiconductor industry benefits from AI processing efficiency advancements.
2. Cryptocurrency market experiences a sharp correction.
3. Global supply chain disruptions impact manufacturing.
4. Company X reports record quarterly earnings.
5. Automotive sector faces challenges due to chip shortages.

## Stock Performance
- **Current Stock Data:**
  - Price: $70.13
  - Sector: Technology
  - Industry: Communication Equipment

- **Historical Stock Data (1 year):**
  - Start Open Price: $54.99
  - End Close Price: $70.13
  - Highest Price: $72.11
  - Lowest Price: $51.49

## Macroeconomic Context
- Consumer Price Index (CPI) data:
  - Apr 2025: 320.32
  - May 2025: 320.58
  - Jun 2025: 321.50
  - Jul 2025: 322.13
  - Aug 2025: 323.36

## Key Financial Filings
No recent 10-K filings found for Cisco.

## Financial Analyst's Outlook
1. **Trends Analysis:**
   - Cisco benefits from semiconductor industry growth and cloud services demand.
2. **Potential Impacts:**
   - Supply chain disruptions may pose operational challenges and cost increases.
3. **Investment Outlook:**
   - **Hold:** Recommended due to positive industry trends and market stability.
   - **Monitor:** Stay informed about supply chain developments and semiconductor market dynamics.

## Conclusion
Cisco's financial performance, industry trends, and market positioning suggest a favorable outlook for investors. Holding positions is recommended, with a focus on monitoring external factors that may impact the company's operations. Cisco's resilience in the technology sector and positive stock performance indicate stability and potential for growth in the future.
======================================================================

######################################################################
### Investment Recommendation for Cisco (CSCO): ###
No specific investment outlook found in the report.
######################################################################

######################################################################
### Financial Analysis System execution finished. ###
######################################################################
## 📜 License

This project is for academic and educational purposes only. All datasets and APIs used are publicly available under their respective licenses.

If you reuse or extend this project, please credit the original contributors.
👥 Authors
Group 11 — AAI520 Final Project
