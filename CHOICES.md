CHOICES

Model Selection

YOLOv8n was selected because it provides a good balance between speed and accuracy for real-time CCTV analytics.

Event Schema Design

JSONL format was chosen because:

- Lightweight
- Easy to stream
- Compatible with analytics pipelines
- Simple to process at scale

API Architecture

A REST-based architecture is proposed for future deployment.

Example endpoints:

GET /visitors

GET /queue

GET /billing

GET /anomalies

Dashboard

Streamlit was selected due to rapid development capability and easy visualization support.
