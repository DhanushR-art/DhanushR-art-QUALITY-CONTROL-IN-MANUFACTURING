# fastapi_app.py
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import numpy as np
import joblib
from backend import get_response  # use the chatbot function

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Load the trained ML model
model = joblib.load("models/defect_model.pkl")

@app.get("/", response_class=HTMLResponse)
async def form_get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": None})

@app.post("/", response_class=HTMLResponse)
async def predict(request: Request, feature1: float = Form(...), feature2: float = Form(...)):
    try:
        features = np.array([[feature1, feature2]])
        prediction = model.predict(features)[0]
        return templates.TemplateResponse("index.html", {"request": request, "result": prediction})
    except Exception as e:
        return templates.TemplateResponse("index.html", {"request": request, "result": f"Error: {str(e)}"})

@app.post("/chat", response_class=HTMLResponse)
async def chat(request: Request, message: str = Form(...)):
    response = get_response(message)
    return templates.TemplateResponse("index.html", {"request": request, "chat_response": response})
