#  AI Sentiment Pulse: Automated News Analysis Dashboard
> **A high-frequency ETL pipeline and real-time sentiment analysis engine for the AI industry.**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ai-sentiment-dashboard-g6l4nvphluyvfal92zxtfd.streamlit.app/)
![Python 3.11](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-Hugging%20Face-yellow)
![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-orange?logo=githubactions)

##  Project Overview
In the fast-moving AI industry, market sentiment shifts daily. This project provides a quantitative **"Mood Metric"** by analyzing real-time news headlines. It identifies if the current market is in a **"Hype Phase"** (Positive) or a **"Regulatory/Fear Phase"** (Negative) based on transformer-based language models.


##  Technical Architecture (The ETL Pipeline)
This project follows a professional **Extract, Transform, Load (ETL)** architecture:

1.  **Extraction**: A Python-based ingestion script fetches real-time headlines from global news APIs.
2.  **Transformation**: Data is processed through **FinBERT** (Financial BERT), a specialized transformer model from Hugging Face that out-performs general NLP models in business contexts.
3.  **Loading**: Processed data (Sentiment Label + Confidence Score) is appended to a persistent CSV database with automatic version control.
4.  **Visualization**: A **Streamlit** frontend pulls from the persistent storage to render live analytics.

##  NLP Logic: Why FinBERT?
Unlike basic libraries like TextBlob, **FinBERT** is pre-trained on a massive corpus of financial text.
* **Precision**: It correctly identifies "Market volatility" or "Regulatory hurdles" as negative, whereas general models often label them as neutral.
* **Confidence Scores**: The system outputs a mathematical probability (e.g., 0.99), ensuring the dashboard only reflects high-certainty data.


##  Automation & DevOps
To ensure 24/7 operation without manual intervention, this project utilizes **GitHub Actions**:
* **CRON Scheduling**: The pipeline triggers every day at 00:00 UTC.
* **Secret Management**: API credentials and environment variables are securely handled via GitHub Secrets.
* **Automated Deployment**: Any push to the `main` branch or a data update via Actions automatically updates the live Streamlit site.

##  Tech Stack
* **Language**: Python 3.11
* **Frameworks**: Streamlit, Plotly
* **Libraries**: Transformers (Hugging Face), PyTorch, Pandas, Requests
* **Infrastructure**: GitHub Actions, Streamlit Cloud

##  Performance Summary
* **Model**: `yiyanghkust/finbert-tone`
* **Avg Confidence**: ~98.9%
* **Data Latency**: Updated daily via automated workflows
