"""
This file contains the main api code
"""
from fastapi import FastAPI
from uvicorn import run

from database.models import generate_schema
from database.parse_json import create_users

app = FastAPI()


if __name__ == "__main__":
    # Generating the database file and schema
    generate_schema()

    # Adding users from json to database
    # create_users()

    # Using uvicorn for creating an ASGI server
    run("api:app", reload=True)
