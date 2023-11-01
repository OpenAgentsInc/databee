"""Hello"""

from fastapi import FastAPI

app = FastAPI(
    title="Parserbee",
    description="Parserbee data magic daemon",
    version="0.1.0"
)

@app.get("/")
async def root():
    """Say hello."""
    return {"message": "Hello World"}
