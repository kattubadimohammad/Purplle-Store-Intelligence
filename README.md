Purplle Store Intelligence System

Overview

This project is an AI-powered Store Intelligence System developed for the Purplle Tech Challenge 2026.

The solution uses computer vision techniques to process CCTV footage and generate store analytics such as visitor monitoring, queue tracking, billing area activity, and operational insights through a dashboard.

Features

- Visitor Detection using YOLOv8
- Customer Footfall Monitoring
- Queue Length Monitoring
- Billing Area Activity Tracking
- Multi-Camera CCTV Support
- Real-Time Dashboard using Streamlit
- Event Logging using JSONL Format

Technology Stack

- Python
- YOLOv8 (Ultralytics)
- OpenCV
- Streamlit
- Pandas
- NumPy

Project Structure

Purplle-Store-Intelligence/
│
├── src/
│   └── detect.py
│
├── app.py
├── README.md
├── DESIGN.md
├── CHOICES.md
├── events.jsonl
└── .gitignore

Installation

Install dependencies:

pip install ultralytics opencv-python streamlit pandas numpy

Running Detection

python src/detect.py

Launch Dashboard

streamlit run app.py

Open the dashboard in your browser:

http://localhost:8501

Dashboard Metrics

The dashboard displays:

- Visitor Count
- Queue Length
- Billing Area Activity
- Operational Insights

Event Logging

Events are stored in JSONL format and can be used for downstream analytics and reporting.

Future Enhancements

- Heatmap Generation
- Anomaly Detection
- Customer Journey Analytics
- Real-Time Event Streaming
- Cloud Deployment

Challenge

Purplle Tech Challenge 2026 – Round 2

Theme: AI-Powered Store Intelligence System

Author

Kattubadi Mohammad
