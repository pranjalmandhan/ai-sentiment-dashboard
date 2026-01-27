import pandas as pd
import requests
import os
from transformers import BertTokenizer, BertForSequenceClassification, pipeline
import torch

# 1. Professional Model Initialization
# We use FinBERT because general models don't understand 'Market Volatility' or 'Bullish Trends'
model_name = "yiyanghkust/finbert-tone"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name)
nlp_pipeline = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

def get_ai_sentiment(text):
    """
    Uses FinBERT to analyze sentiment with high precision.
    """
    try:
        # FinBERT provides labels like 'Positive', 'Negative', and 'Neutral'
        result = nlp_pipeline(text[:512])[0] # Limit to 512 tokens for BERT
        return result['label'], result['score']
    except Exception as e:
        print(f"Error analyzing sentiment: {e}")
        return "Neutral", 0.0

def ingest_data():
    # 2. Secure API Key Management
    # Never hardcode keys; use GitHub Secrets/Environment Variables
    api_key = os.getenv('NEWS_API_KEY')
    if not api_key:
        print("Missing API Key. Ensure NEWS_API_KEY is set in environment.")
        return

    url = f'https://newsapi.org/v2/everything?q=Artificial Intelligence&apiKey={api_key}'
    
    try:
        response = requests.get(url)
        data = response.json()
        articles = data.get('articles', [])
        
        processed_data = []
        for article in articles[:20]: # Process top 20 news items
            title = article['title']
            label, score = get_ai_sentiment(title)
            
            processed_data.append({
                'date': pd.to_datetime('today').strftime('%Y-%m-%d'),
                'title': title,
                'sentiment': label,
                'confidence': score,
                'source': article['source']['name']
            })
        
        # 3. Data Persistence & Versioning
        new_df = pd.DataFrame(processed_data)
        file_path = 'data/daily_sentiment.csv'
        
        # Append to existing data or create new
        if os.path.exists(file_path):
            existing_df = pd.read_csv(file_path)
            updated_df = pd.concat([existing_df, new_df], ignore_index=True)
            updated_df.to_csv(file_path, index=False)
        else:
            new_df.to_csv(file_path, index=False)
            
        print(f"Successfully ingested {len(processed_data)} news items.")

    except Exception as e:
        print(f"Pipeline failed: {e}")

if __name__ == "__main__":
    ingest_data()
