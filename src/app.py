import streamlit as st
import pandas as pd


st.set_page_config(page_title="AI Sentiment Tracker", layout="wide")
st.title("🤖 AI News Sentiment & Trend Analysis")


try:
    df = pd.read_csv('data/daily_sentiment.csv')
    df['date'] = pd.to_datetime(df['date']) # Ensure date is a date object
    
 
    st.sidebar.header("Filter Options")
    search_query = st.sidebar.text_input("Search Headlines", "")
    
    if search_query:
        df = df[df['title'].str.contains(search_query, case=False)]

    avg_sentiment = df['sentiment_score'].mean()
    col1, col2 = st.columns(2)
    col1.metric("Average Mood", f"{avg_sentiment:.2f}")
    col2.metric("Total Headlines Analyzed", len(df))

    st.subheader("Sentiment Trend Over Time")
    chart_data = df.groupby('date')['sentiment_score'].mean()
    st.line_chart(chart_data)

    st.subheader("Latest News Data")
    st.dataframe(df.sort_values(by='date', ascending=False), use_container_width=True)

except FileNotFoundError:
    st.error("⚠️ Data file not found. Please run the GitHub Action first!")
