import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv
from tools import search_crypto_news, get_crypto_price, search_sentiment

load_dotenv()

# Page config
st.set_page_config(
    page_title="DeFi Research Agent",
    page_icon="🔍",
    layout="centered"
)

# Header
st.title("🔍 DeFi Research Agent")
st.markdown("*AI-powered crypto research — real-time price, news & sentiment analysis*")
st.divider()

# Input
token = st.text_input("Enter a crypto token name", placeholder="e.g. bitcoin, ethereum, solana")
search_btn = st.button("🚀 Research Now", use_container_width=True)

if search_btn and token:
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    # Price
    with st.spinner("📈 Fetching price data..."):
        price_data = get_crypto_price(token.strip().lower())

    st.subheader("📈 Price Data")
    st.code(price_data)

    # News
    with st.spinner("📰 Fetching latest news..."):
        news_data = search_crypto_news(token.strip().lower())

    # Sentiment
    with st.spinner("💬 Analyzing sentiment..."):
        sentiment_data = search_sentiment(token.strip().lower())

    # AI Analysis
    with st.spinner("🤖 Generating AI research report..."):
        prompt = f"""
Analyze the following data for {token.upper()} and provide a structured research report.

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
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional DeFi research analyst."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=1000
        )
        report = response.choices[0].message.content

    st.subheader("🤖 AI Research Report")
    st.markdown(report)
    st.divider()
    st.caption("⚠️ This is not financial advice. Always do your own research.")

elif search_btn and not token:
    st.warning("Please enter a token name!")