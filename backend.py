import pandas as pd
import uvicorn
import json
from fastapi import FastAPI
from api_model import UserPredDate
from ml_model import load_model_and_predict

app = FastAPI()

# Route to add a date for a prediction
@app.post("/predict")
# A function that loads the serialized prophet model and returns a prediction as a response 
def make_prediction(date: UserPredDate) -> dict[str, str]:
    year = date.year
    month = date.month
    prediction_date = str(year +"-"+ month +"-"+"01")
    value = load_model_and_predict(prediction_date)
    return {"prediction":str(value)}