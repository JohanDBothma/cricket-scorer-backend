import os
import sys

from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)

# Get the absolute path to the project directory
project_dir = os.path.abspath(os.path.dirname(__file__))

# Add the project directory to the Python path
sys.path.insert(0, project_dir)

# Configure the app
app.config["MONGO_URI"] = os.environ.get("MONGO_URI", "mongodb://localhost:27017/cricket-scorer")
mongo = PyMongo(app)
CORS(app)

# Import routes
from app import routes

if __name__ == '__main__':
    app.run(debug=True)