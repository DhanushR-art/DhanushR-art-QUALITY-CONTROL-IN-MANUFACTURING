#!/bin/bash

# Activate venv
source .venv/bin/activate

# Run FastAPI (backend) on port 8000
echo "🔁 Starting FastAPI backend..."
uvicorn fastapi_app:app --reload &

# Run Streamlit (frontend) on port 8501
echo "💬 Launching Streamlit chatbot..."
streamlit run streamlit_app.py
