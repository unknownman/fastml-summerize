from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from summarizer import Summarizer

app = FastAPI()


class Input(BaseModel):
    text: str
    lang: str
    summerized: str = None
    score: float = None


class Output(BaseModel):
    summerized: str
    score: float


summarizer = Summarizer()


@app.post("/summarize", response_model=Output)
async def summarize(input_data: Input):
    if input_data.lang == "fa":
        # tokenize and preprocess Persian text
        input_data.text = summarizer.extract_text(input_data.text)
        input_data.text = summarizer.preprocess(input_data.text)

    # generate summary
    summary = summarizer.generate_summary(input_data.text)

    # return summary as output
    output = {"summerized": summary}
    return output


@app.post("/score", response_model=Output)
async def score(input_data: Input):
    if not input_data.summerized:
        raise HTTPException(
            status_code=400, detail="Summerized text is required for scoring.")

    if input_data.lang == "fa":
        # tokenize and preprocess Persian text
        input_data.text = summarizer.extract_text(input_data.text)
        input_data.text = summarizer.preprocess(input_data.text)
        input_data.summerized = summarizer.extract_text(input_data.summerized)
        input_data.summerized = summarizer.preprocess(input_data.summerized)

    # calculate score
    score = summarizer.calculate_score(input_data.text, input_data.summerized)

    # return score as output
    output = {"summerized": input_data.summerized, "score": score}
    return output


@app.post("/learn")
async def learn(input_data: Input):
    # add code here to train model
    return {"message": "Model training successful."}
