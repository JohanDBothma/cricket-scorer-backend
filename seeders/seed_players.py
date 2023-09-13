from app.database import mongo

# Define the data you want to insert
player_data = [
    {"name": "A"},
    {"name": "B"},
]

def seed_players():
    # Access the 'players' collection
    players_collection = mongo.db.players

    # Insert data into the 'players' collection
    inserted_data = players_collection.insert_many(player_data)

    # Print a message indicating the number of documents inserted
    print(f"Inserted {len(inserted_data.inserted_ids)} documents into 'players' collection")

seed_players()