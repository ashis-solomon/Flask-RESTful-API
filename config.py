import os

class Config:
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb://localhost:27017/'
    DB_NAME = os.environ.get('DB_NAME') or 'db'
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME') or 'users_db'