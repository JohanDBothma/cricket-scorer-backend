from flask_pymongo import PyMongo

# Create a PyMongo instance
mongo = PyMongo()

def init_db(app):
    # Initialize the database connection
    mongo.init_app(app)
