import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'AAA!!!BBBCCC@@@@!!!!'
    DEBUG = True
    TESTING = False

    MONGODB_URI = os.environ.get('MONGODB_URI') or 'mongodb://localhost:27017/db'
    MONGODB_NAME = os.environ.get('MONGODB_NAME') or 'db'

    BASE_URL = 'http://127.0.0.1:5000'
