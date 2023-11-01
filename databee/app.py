"""Hello"""

from fastapi import FastAPI
from databee.ingest import ingest_pdf

app = FastAPI(
    title="Databee",
    description="Databee data magic daemon",
    version="0.1.0"
)

@app.get("/")
async def root():
    """Say hello."""
    return {"message": "Hello from databee"}

@app.get("/test")
async def test():
    """Let's try ingesting a PDF"""
    doc = ingest_pdf("docs/Seasteading-Implementation-Plan.pdf")
    return {"message": doc[9]}
