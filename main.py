from fastapi import FastAPI

app = FastAPI()


@app.get("/ready")
def Ready():
    return {"Status Code": "200", "MSG": "HTTP:/2.0"}

@app.post('/fraud-score')
def Fraud_Score():
    return {}