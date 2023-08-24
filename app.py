from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mydatabase"
mongo = PyMongo(app)

@app.route('/insert', methods=['POST'])
def insert_data():
    data = request.json
    collection = mongo.db.my_collection
    inserted_data = collection.insert_one(data)
    return jsonify({"message": "Data inserted successfully", "id": str(inserted_data.inserted_id)})

if __name__ == '__main__':
    app.run(debug=True)
