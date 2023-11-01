"""Hello"""

from fastapi import FastAPI

app = FastAPI(
    title="Databee",
    description="Databee data magic daemon",
    version="0.1.0"
)

@app.get("/")
async def root():
    """Say hello."""
    return {"message": "Hello from databee"}
