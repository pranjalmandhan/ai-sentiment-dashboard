import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="AI Sentiment Pulse Pro", layout="wide")
st.title("AI Sentiment Pulse: Market Mood Dashboard")

try:
    df = pd.read_csv('data/daily_sentiment.csv')
    
    # KPIs
    c1, c2, c3 = st.columns(3)
    c1.metric("Dominant Mood", df['sentiment'].mode()[0])
    c2.metric("AI Confidence", f"{df['confidence'].mean()*100:.1f}%")
    c3.metric("Articles", len(df))

    # Visualization
    fig = px.pie(df, names='sentiment', color='sentiment', 
                 color_discrete_map={'Positive': '#00CC96', 'Neutral': '#636EFA', 'Negative': '#EF553B'},
                 hole=0.4, title="Market Sentiment Distribution")
    st.plotly_chart(fig, use_container_width=True)

    # Raw Data
    st.dataframe(df.sort_values(by='date', ascending=False), use_container_width=True)

except:
    st.warning("Waiting for the first data update from GitHub Actions...")
