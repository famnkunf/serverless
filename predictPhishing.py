import joblib
import pandas as pd
from fastapi import FastAPI

app = FastAPI()

def predictPhishing(url):
    model = joblib.load('model.pkl')
    df = pd.DataFrame([url])
    df.columns = ['url']
    return model.predict(df["url"])[0]

@app.get('/predict')
async def predict(url: str):
    if predictPhishing(url) ==1:
        message = 'Phishing'
    else:
        message = 'Not Phishing'
    return {'message': message}

