import pandas as pd
from textblob import TextBlob
import datetime
import random

def get_sentiment(text):
    return round(TextBlob(text).sentiment.polarity, 2)

dates = [(datetime.date.today() - datetime.timedelta(days=i)) for i in range(7)]
headlines = [
    "AI breakthroughs in medicine", "Concerns over AI privacy", 
    "New robots powered by AI", "AI startup funding peaks",
    "Regulation debates for AI", "AI in schools discussed", "Future of AI looks bright"
]

all_data = []

for d in dates:
  
    daily_titles = random.sample(headlines, 3)
    for title in daily_titles:
        all_data.append({
            'date': d,
            'title': title,
            'sentiment_score': get_sentiment(title)
        })


df = pd.DataFrame(all_data)
df.to_csv('data/daily_sentiment.csv', index=False)
print("7-day historical data generated successfully!")
