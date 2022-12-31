"""
This file contains the main api code
"""
from fastapi import FastAPI
from uvicorn import run

from database.models import generate_schema
from database.parse_json import create_users
from database.db import Database

app = FastAPI()
db = Database()

## <<----------------------------------------------------->>
## CRUD Routes

# Fetching user from ID
@app.get("/{id}")
async def get_user(id: int):
    user = db.fetch_user_by_id(id)
    # Do Stuff
    return {"data": f"Hello, {user.name}..!"}

# Creating new user
@app.post("/create-user")
async def create_user():
    ...

# Deleting an existing user
@app.delete("/{id}")
async def delete_user(id: int):
    ...


if __name__ == "__main__":
    # Generating the database file and schema
    generate_schema()

    # Adding users from json to database
    # create_users()

    # Using uvicorn for creating an ASGI server
    run("api:app", reload=True)
