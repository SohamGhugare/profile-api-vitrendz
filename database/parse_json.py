"""
This file contains the code for parsing the json provided in the problem statement
Note: The repo doesnt contain the downloaded json file for storage purposes.
"""
import json
from typing import List

from .models import User
from .db import Database

with open("generated.json", "r") as f:
    data = json.load(f)

def parse() -> List[User]:
    users = []

    for d in data:
        user = User(
            guid = d["guid"],
            is_active = True if d["isActive"]=="true" else False,
            balance = float(d["balance"][1:].replace(",", "")),
            picture = d["picture"],
            age = int(d["age"]),
            eye_color = d["eyeColor"],
            name = d["name"],
            gender = d["gender"],
            company = d["company"],
            email = d["email"],
            phone = d["phone"],
            address = d["address"],
            about = d["about"],
            registered = d["registered"],
            latitude = float(d["latitude"]),
            longitude = float(d["longitude"]),
            tags = d["tags"],
            friends = [f["name"] for f in d["friends"]],
            greeting=d["greeting"]
        )
        users.append(user)
        
    return users

def create_users():
    users = parse()
    db = Database()

    for user in users:
        name = db.create_user(user)
        print(f"Added {name}")
    print(users[0])

