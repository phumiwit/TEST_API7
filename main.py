from fastapi import FastAPI
from pydantic import BaseModel
from key import Keyword_Spotting_Service
import uvicorn
app = FastAPI()




    
@app.get('/')
def Hello():
    return {'Hello':'Hello'}

@app.post('/predict')
def predict_genre(path:str):
    
    kss = Keyword_Spotting_Service()
    keyword1,keyword2= kss.prediction(path)
    return {"prediction":keyword1}

@app.post('/value',)
def value_genre(path : str):
    kss = Keyword_Spotting_Service()
    keyword1,keyword2 = kss.prediction(path)
    
    return keyword2


