import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-secret-key'
    DB_NAME = 'db'
    MONGODB_URI = os.environ.get('MONGODB_URI') or 'mongodb://localhost:27017/db'
    DEBUG = True
    TESTING = False