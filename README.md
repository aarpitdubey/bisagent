# Agentic AI Application for Industrial Analysis

## 📌 Overview

This application automates data visualization and AI/ML analysis using **Agentic AI (CrewAI)**. It processes industrial data, performs **clustering, anomaly detection, and industrial hotspot prediction**, and provides interactive dashboards.

## 🏗️ Features

- **Upload CSV Dataset** 📂
- **Data Cleaning & Preprocessing** 🧹
- **Industry Distribution Analysis** 📊
- **Geospatial Visualization (Folium)** 🗺️
- **Clustering & Anomaly Detection** 🚀
- **Industrial Hotspot Prediction (ML Model)** 🔥

## 📁 Folder Structure

```
/bisagent
├── src/  # Main application code
│   ├── main.py  # Streamlit UI
│   ├── dashboard.py  # Data visualization logic
│   ├── model.py  # AI/ML model implementations
│   ├── upload.py  # Handles CSV upload & processing
│
├── agents/  # CrewAI agent definitions
│   ├── data_cleaning.py
│   ├── visualization.py
│   ├── hotspot_prediction.py
│
├── data/  # Stores datasets
│   ├── other_industries_original_unaltered.csv
│   ├── uploaded_data.csv
│
├── utils/  # Helper functions
│   ├── data_processing.py
│   ├── model_training.py
│
├── requirements.txt  # Dependencies
├── README.md  # Documentation & User Guide
├── Dockerfile  # Containerization for deployment
```

## 🚀 Installation

```bash
git clone https://github.com/your-repo/bisagent.git
cd bisagent
pip install -r requirements.txt
streamlit run src/main.py
```

## 🐳 Deploy with Docker

```bash
docker build -t bisagent .
docker run -p 8501:8501 bisagent
```

## 🌐 Deploy on Streamlit Cloud

1. Push to GitHub.
2. Go to [Streamlit Cloud](https://share.streamlit.io/).
3. Deploy using `app/main.py`.

## 💡 Usage Guide

- **Upload dataset** or use default data.
- **Select a task** (Data Cleaning, Visualization, Prediction).
- **View insights, charts, and business conclusions.**

## 🤝 Contributing

PRs are welcome! Open an issue for discussions.

## 📝 License

GNU License
