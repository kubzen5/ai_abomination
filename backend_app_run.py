import uvicorn
from fastapi import FastAPI
import os

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(
        app,
        host=os.getenv("API_HOST", "0.0.0.0"),
        port=int(os.getenv("API_PORT", "8080")),
    )