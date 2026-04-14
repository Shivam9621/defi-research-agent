# 🔍 DeFi Research Agent

An AI-powered agent that researches any cryptocurrency token in real-time and generates a professional research report.

## What it does
- Fetches live price data from CoinGecko
- Searches latest news using Tavily
- Analyzes community sentiment
- Generates a structured Buy/Hold/Avoid report using LLaMA 3.3 (Groq)

## How to run

1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Add your API keys to `.env`:

GROQ_API_KEY=your_key
TAVILY_API_KEY=your_key

5. Run: `python agent.py`

## Example Output
🔍 Researching: BITCOIN
📈 Fetching price data...
📰 Fetching latest news...
💬 Fetching community sentiment...
🤖 Analyzing with AI...
Verdict: Hold — Strong fundamentals but short-term uncertainty remains.
## Tech Stack
- Python
- Groq API (LLaMA 3.3-70b)
- Tavily Search API
- CoinGecko API

Save with Ctrl + S, then run:
pip freeze > requirements.txt
git add .
git commit -m "Add README and requirements"
git push
