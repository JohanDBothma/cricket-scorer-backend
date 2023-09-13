import bcrypt
from app.database import mongo

# Password to be hashed
password = "admin"

# Generate a salt and hash the password
salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

administrators = [
    {
        "name": "Johan",
        "surname": "Bothma",
        "is_admin": 1,
        "email": "admin@email.com",
        "password": hashed_password
    },
]

def seed_admins():
    players_collection = mongo.db.players
    inserted_data = players_collection.insert_many(administrators)
    print(f"Inserted {len(inserted_data.inserted_ids)} admins into 'players' collection")

seed_admins()