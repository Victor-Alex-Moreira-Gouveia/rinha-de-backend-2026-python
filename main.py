from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    nome: str
    profissao: Optional[str] = None

app = FastAPI()

@app.get("/ready")
def Ready():
    return {"Status Code": "200", "MSG": "HTTP 2xx"}

@app.post('/fraud-score')
def Fraud_Score(item: Item):
    return {"Mensagem": "Item criado com sucesso", "Item": item}