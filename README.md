# Interstellar Audience Analysis Project 🚀

This academic project analyzes the audience of the movie *Interstellar* using Big Data, Natural Language Processing (NLP), and Machine Learning techniques. It compares the "General Audience" (YouTube) with "Cinephiles" (IMDb) to uncover deep insights into viewer motivations and sentiment.

## 📊 Overview

The project segments the audience into distinct profiles (Fans, Science Geeks, Confusion, Casuals) and provides strategic marketing recommendations based on data-driven insights.

## 🛠 Tech Stack

*   **Python 3.14**
*   **Data Collection:** YouTube Data API, Browser Automation (for IMDb)
*   **NLP:** `sentence-transformers` (Embeddings), `transformers` (Sentiment Analysis)
*   **Clustering:** K-Means
*   **Dimensionality Reduction:** PCA
*   **Visualization:** Matplotlib, Seaborn

## 📂 Project Structure

*   `scripts/`: Python scripts for scraping, analysis, and visualization.
*   `data/`: Raw and processed data (Note: Raw data is not included in the repo).
*   `outputs/`: Generated reports and visualization charts.

## 🚀 How to Run

1.  **Clone the repository**
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the analysis:**
    *   To scrape IMDb (optional): `python scripts/imdb_mass_scrape.py`
    *   To run comparison: `python scripts/step26_compare_imdb_youtube.py`
    *   To generate HTML report: `python scripts/export_report_html.py`

## 📄 Report

The final academic report is available in the `outputs/` directory.

---
*Created for Academic Analysis Purposes - January 2026*
