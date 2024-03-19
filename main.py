from typing import Dict
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pandas import DataFrame
import uvicorn

from services.load_data_service import read_from_csv

app = FastAPI(title="Power Plants API", version="0.0.1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)


@app.get("/")
def read_root() -> Dict[str, str]:
    return {"health": "OK"}


@app.post("/load-data", response_model=None)
def handle_data_load() -> DataFrame:
    read_from_csv()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
