import requests
import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_crypto_news(token_name: str) -> str:
    """Search for latest news about a crypto token"""
    try:
        results = tavily.search(
            query=f"{token_name} cryptocurrency latest news 2026",
            max_results=5
        )
        news = ""
        for r in results["results"]:
            news += f"- {r['title']}: {r['content'][:200]}\n\n"
        return news if news else "No news found."
    except Exception as e:
        return f"Error fetching news: {str(e)}"


def get_crypto_price(token_name: str) -> str:
    """Get current price of a crypto token from CoinGecko (free, no API key)"""
    try:
        # First search for the coin id
        search_url = f"https://api.coingecko.com/api/v3/search?query={token_name}"
        search_res = requests.get(search_url, timeout=10).json()
        
        if not search_res["coins"]:
            return f"Could not find price data for {token_name}"
        
        coin_id = search_res["coins"][0]["id"]
        
        # Then get price
        price_url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd&include_24hr_change=true&include_market_cap=true"
        price_res = requests.get(price_url, timeout=10).json()
        
        data = price_res[coin_id]
        return (
            f"Token: {token_name.upper()}\n"
            f"Price: ${data['usd']:,.4f}\n"
            f"24h Change: {data['usd_24h_change']:.2f}%\n"
            f"Market Cap: ${data['usd_market_cap']:,.0f}"
        )
    except Exception as e:
        return f"Error fetching price: {str(e)}"


def search_sentiment(token_name: str) -> str:
    """Search for community sentiment about a token"""
    try:
        results = tavily.search(
            query=f"{token_name} crypto sentiment bullish bearish community 2026",
            max_results=4
        )
        sentiment = ""
        for r in results["results"]:
            sentiment += f"- {r['title']}: {r['content'][:200]}\n\n"
        return sentiment if sentiment else "No sentiment data found."
    except Exception as e:
        return f"Error fetching sentiment: {str(e)}"