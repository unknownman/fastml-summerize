from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
from typing import List
import torch
from summarizer import Summarizer

app = FastAPI()


class InputData(BaseModel):
    text: str
    lang: str
    summerized: str


class OutputData(BaseModel):
    score: float


@app.post("/score")
async def score_text(input_data: InputData):
    if input_data.lang != 'fa':
        raise HTTPException(
            status_code=400, detail="Invalid Language. Currently, only Persian language is supported.")

    model = Summarizer(input_data.summerized)
    score = model(input_data.text, ratio=len(
        input_data.summerized)/len(input_data.text))

    return {'score': score}
