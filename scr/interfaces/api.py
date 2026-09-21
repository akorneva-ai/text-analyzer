from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware
import time
from scr.infrastructure.text_analiser import Text_Analyzer

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

analyzer = Text_Analyzer()

@app.post("/analyze")
async def analyze(request: AnalyzeRequest):
    return analyzer.analyze(request.text)

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

        return [analyzer.analyze(text) for text in request.texts]

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )
