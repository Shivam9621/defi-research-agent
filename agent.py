import os
from groq import Groq
from dotenv import load_dotenv
from tools import search_crypto_news, get_crypto_price, search_sentiment

load_dotenv()

# Configure Groq
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_ai(prompt: str) -> str:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a professional DeFi research analyst. Provide clear, structured, and insightful crypto research reports."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
        max_tokens=1000
    )
    return response.choices[0].message.content

def run_agent(token_name: str):
    print(f"\n{'='*50}")
    print(f"🔍 Researching: {token_name.upper()}")
    print(f"{'='*50}\n")

    # Step 1: Get price
    print("📈 Fetching price data...")
    price_data = get_crypto_price(token_name)
    print(price_data)

    # Step 2: Get news
    print("\n📰 Fetching latest news...")
    news_data = search_crypto_news(token_name)

    # Step 3: Get sentiment
    print("💬 Fetching community sentiment...")
    sentiment_data = search_sentiment(token_name)

    # Step 4: Ask AI to analyze everything
    print("\n🤖 Analyzing with AI...\n")

    prompt = f"""
Analyze the following data for {token_name.upper()} and provide a structured research report.

PRICE DATA:
{price_data}

LATEST NEWS:
{news_data}

COMMUNITY SENTIMENT:
{sentiment_data}

Please provide:
1. **Summary** - What is happening with this token right now?
2. **Bullish Signals** - What looks positive?
3. **Bearish Risks** - What are the risks?
4. **Verdict** - Buy / Hold / Avoid with a brief reason

Keep it concise and professional.
"""

    result = ask_ai(prompt)
    print(result)
    print(f"\n{'='*50}\n")

if __name__ == "__main__":
    token = input("Enter crypto token name (e.g. bitcoin, solana, ethereum): ")
    run_agent(token.strip().lower())