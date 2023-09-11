from flask import jsonify, request
from app import app, mongo
from app.database import init_db

# Initialize the database connection
init_db(app)

@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Flask app is running"})

@app.route('/players', methods=['GET'])
def get_players():
    players_collection = mongo.db.players
    players = list(players_collection.find())
    return jsonify(players)

@app.route('/insert', methods=['POST'])
def insert_player():
    data = request.json
    players_collection = mongo.db.players
    inserted_data = players_collection.insert_one(data)
    return jsonify({"message": "Data inserted successfully", "id": str(inserted_data.inserted_id)})
