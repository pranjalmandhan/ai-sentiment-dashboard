import pandas as pd
import requests
import os
from transformers import BertTokenizer, BertForSequenceClassification, pipeline

# Load the professional FinBERT model
model_name = "yiyanghkust/finbert-tone"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name)
nlp_pipeline = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

def get_ai_sentiment(text):
    try:
        # BERT has a 512-token limit
        result = nlp_pipeline(text[:512])[0] 
        return result['label'], result['score']
    except:
        return "Neutral", 0.0

def ingest_data():
    api_key = os.getenv('NEWS_API_KEY')
    if not api_key:
        print("Error: NEWS_API_KEY not found.")
        return

    url = f'https://newsapi.org/v2/everything?q=Artificial Intelligence&apiKey={api_key}'
    
    try:
        response = requests.get(url)
        articles = response.json().get('articles', [])
        
        processed_data = []
        for article in articles[:20]:
            label, score = get_ai_sentiment(article['title'])
            processed_data.append({
                'date': pd.to_datetime('today').strftime('%Y-%m-%d'),
                'title': article['title'],
                'sentiment': label,
                'confidence': score,
                'source': article['source']['name']
            })
        
        df = pd.DataFrame(processed_data)
        file_path = 'data/daily_sentiment.csv'
        
        # Persistence logic
        if os.path.exists(file_path):
            existing_df = pd.read_csv(file_path)
            pd.concat([existing_df, df], ignore_index=True).to_csv(file_path, index=False)
        else:
            df.to_csv(file_path, index=False)
            
        print("Success: Data saved.")
    except Exception as e:
        print(f"Failed: {e}")

if __name__ == "__main__":
    ingest_data()
