from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from textblob import TextBlob
import time

app = FastAPI()

@app.middleware("http")
async def log_requests(request, call_next):
    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time

    print(
        f"{request.method} {request.url.path} "
        f"- {response.status_code} "
        f"- {process_time:.4f} sec"
    )

    return response


class AnalyzeRequest(BaseModel):
    text: str = Field(..., min_length=1)


class BatchAnalyzeRequest(BaseModel):
    texts: list[str] = Field(..., min_length=1)


def analyze_text(text: str):
    try:
        # Проверяем, что текст не состоит только из пробелов
        if not text.strip():
            raise HTTPException(
                status_code=400,
                detail="Text cannot be empty"
            )

        blob = TextBlob(text)

        return {
            "text": text,
            "polarity": blob.sentiment.polarity,
            "subjectivity": blob.sentiment.subjectivity
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )


@app.post("/analyze")
def analyze(request: AnalyzeRequest):
    return analyze_text(request.text)


@app.post("/analyze-batch")
def analyze_batch(request: BatchAnalyzeRequest):
    try:
        # Проверяем каждый текст
        for text in request.texts:
            if not text.strip():
                raise HTTPException(
                    status_code=400,
                    detail="Texts cannot contain empty strings"
                )

        return [analyze_text(text) for text in request.texts]

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )