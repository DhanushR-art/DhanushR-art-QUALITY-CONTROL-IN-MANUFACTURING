IBM NAAN MUDHALVAN QUALITY CONTROL IN MANUFACTURING

# 🧠 AI-EBPL – Quality Control in Manufacturing

This project leverages Artificial Intelligence (AI) and Emerging Best Practices & Learnings (EBPL) to enhance **quality control** in manufacturing. It includes a **Streamlit-based chatbot**, a **FastAPI-powered backend**, and a **machine learning model** for defect prediction.

---

## 📦 Key Features

- 🤖 **Chatbot using ChatterBot** to answer manufacturing-related queries.
- 🧪 **ML-based defect prediction** using a RandomForestClassifier.
- 🌐 **FastAPI** for backend services including chatbot and prediction endpoints.
- 🖥️ **Streamlit frontend** for intuitive chat interface.
- 🧹 **Data preprocessing and training scripts** for custom model generation.

---

## 📁 Project Structure


---

## 🚀 How to Run the Project

### 1. 📥 Clone & Set Up Environment

```bash
git clone https://github.com/yourusername/ai-ebpl-quality-control.git
cd ai-ebpl-quality-control
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
pip install pydantic==1.10.12  # Fix for ChatterBot dependencies
Train Your Model (Optional)
python src/create_defect_model.py   # Quick mock data
# or
python src/train.py                 # Full dataset training
uvicorn fastapi_app:app --reload
# Visit: http://127.0.0.1:8000
streamlit run streamlit_app.py
# Visit: http://localhost:8501
📊 Machine Learning Model
A simple RandomForestClassifier is trained on features like:

Defect type

Repair cost

Severity

Inspection method

The model is saved as models/defect_model.pkl.

🤖 Chatbot (ChatterBot)
Initialized with English corpus from chatterbot.corpus.english

Answers quality control and production-related queries

Easily extendable with your own training data

🌍 Future Enhancements
Add OpenAI/Gemini LLM integration for smarter chatbot

Visual defect detection with computer vision

Real-time sensor monitoring via IoT

Advanced analytics and dashboards with Plotly

🪪 License
This project is licensed under the MIT License.
For feedback or feature requests, feel free to open an issue or PR.

yaml
Copy
Edit

---

Would you like me to package this in your repo structure or include badges (build, license, author, etc.)?
