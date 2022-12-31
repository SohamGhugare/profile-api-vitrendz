"""
This file contains the main api code
"""
from fastapi import FastAPI
from uvicorn import run

app = FastAPI()


if __name__ == "__main__":
    # Using uvicorn for creating an ASGI server
    run("api:app", reload=True)