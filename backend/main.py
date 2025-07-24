from fastapi import FastAPI
import os

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api")
def read_root():
    return {"message": "Let's craft a professional profile from your spreadsheet"}

@app.get("/env")
def read_env():
    return {
        "ENV": os.getenv("ENV", "not set"),
    }
