import os
from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)

# Configure the app
app.config["MONGO_URI"] = os.environ.get("MONGO_URI", "mongodb://localhost:27017/cricket-scorer")
mongo = PyMongo(app)
CORS(app)

# Import routes
from app import routes
