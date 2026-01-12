import requests
import pandas as pd
from textblob import TextBlob
import datetime

QUERY = 'Artificial Intelligence'
def get_sentiment(text):
    analysis = TextBlob(text)
    return round(analysis.sentiment.polarity, 2)

data = {
    'date': [datetime.date.today()] * 3,
    'title': [
        "New AI model breaks benchmarks in medical science",
        "Experts warn of job losses due to AI automation",
        "AI startup raises $100 million in latest funding round"
    ],
    'source': ["TechHealth", "GlobalNews", "BusinessWeekly"]
}

df = pd.DataFrame(data)
df['sentiment_score'] = df['title'].apply(get_sentiment)

df.to_csv('data/daily_sentiment.csv', index=False)
print("Data successfully ingested and saved!")
