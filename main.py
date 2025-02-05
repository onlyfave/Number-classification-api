from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get("/api/classify-number")
def classify_number(number: int = Query(..., description="Number to classify")):
    return {"message": f"You entered {number}!"}

