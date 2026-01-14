# 🤖 AI Sentiment Pulse: Automated News Analysis Dashboard
[![Live App](https://img.shields.io/badge/Status-Live_Dashboard-brightgreen)](PASTE_YOUR_STREAMLIT_URL_HERE)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Automation](https://img.shields.io/badge/Pipeline-GitHub_Actions-orange)](https://github.com/features/actions)

## Business Case
In the fast-paced AI industry, market sentiment shifts daily. This project provides a **quantifiable "Mood Metric"** by analyzing real-time news headlines. It helps stakeholders identify if the industry is currently in a "Hype" phase (positive) or a "Regulatory/Fear" phase (negative).

### Key Insights
- **Automated Trend Detection:** Tracks sentiment fluctuations across 20+ headlines daily.
- **Industry Pulse:** Calculated a current average sentiment score of **0.04**, indicating a neutral-to-positive market outlook.

## Technical Stack
- **Languages:** Python (Pandas for data manipulation).
- **NLP:** TextBlob for Natural Language Processing (Polarity Scoring).
- **Frontend:** Streamlit for interactive data visualization.
- **Automation:** GitHub Actions CI/CD pipeline for daily data ingestion.

## Project Structure
- `src/app.py`: The interactive dashboard code.
- `src/ingest.py`: The data collection and NLP processing engine.
- `data/daily_sentiment.csv`: Automated time-series storage.
- `.github/workflows/`: Automation scripts for 24/7 updates.

## How to Run Locally
1. Clone this repo: `git clone https://github.com/YOUR_USERNAME/ai-sentiment-dashboard.git`.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run the dashboard: `streamlit run src/app.py`.

---
*Created as part of my Data Analyst Portfolio to demonstrate end-to-end pipeline development.*
