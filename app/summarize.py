from fastapi import APIRouter, HTTPException, Body
from typing import List
from .summarizer import Summarizer

router = APIRouter()


@router.post("/summarize")
async def summarize_text(text: str = Body(...), lang: str = Body(...)):
    """
    Returns a summarized version of the input text.
    """
    try:
        summarizer = Summarizer(lang=lang)
        summary = summarizer.summarize(text)
        return {"summary": summary}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
