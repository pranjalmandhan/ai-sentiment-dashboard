import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Sentiment Tracker", page_icon="🤖")

st.title("AI News Sentiment Dashboard")
st.markdown("This dashboard tracks the mood of the latest AI news headlines.")

try:
    df = pd.read_csv('data/daily_sentiment.csv')
   
    avg_score = df['sentiment_score'].mean()
    st.metric(label="Average Sentiment Score", value=avg_score, delta="Positive" if avg_score > 0 else "Negative")

    st.subheader("Latest Headlines & Scores")
    st.dataframe(df)

    st.subheader("Sentiment Distribution")
    st.bar_chart(df['sentiment_score'])

except FileNotFoundError:
    st.error("No data found! Please run the ingest script first.")
