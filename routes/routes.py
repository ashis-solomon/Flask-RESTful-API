from flask import Blueprint, jsonify, request
from pymongo import MongoClient
from config import Config
from models.models import User
import uuid

user_routes = Blueprint('user_routes', __name__)
mongo = MongoClient(Config.MONGODB_URI)

# index
@user_routes.route('/')
def index():
    return jsonify({'message': 'OK'})


# GET all users
@user_routes.route('/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    output = [User.from_dict(user_dict) for user_dict in users]
    return jsonify({'message': [user.to_dict() for user in output]})


# GET user by ID
@user_routes.route('/users/<id>', methods=['GET'])
def get_user(id):
    user_dict = mongo.db.users.find_one({'id': id})
    if user_dict:
        user = User.from_dict(user_dict)
        output = user.to_dict()
    else:
        output = "No such user found"
    return jsonify({'message': output})


# POST new user
@user_routes.route('/users', methods=['POST'])
def add_user():
    user_dict = request.json
    new_id = str(uuid.uuid4())
    user = User(id=new_id, name=user_dict['name'], email=user_dict['email'], password=user_dict['password'])
    existing_user_dict = mongo.db.users.find_one({'email': user.email})
    if existing_user_dict:
        return jsonify({'error': 'User with this email already exists'})
    mongo.db.users.insert_one(user.to_dict())

    return jsonify({'message': user.to_dict()})


# PUT update user by ID
@user_routes.route('/users/<id>', methods=['PUT'])
def update_user(id):
    user_dict = mongo.db.users.find_one({'id': id})
    if user_dict:
        user = User.from_dict(user_dict)
        user.name = request.json.get('name', user.name)
        user.email = request.json.get('email', user.email)
        user.password = request.json.get('password', user.password)

        mongo.db.users.update_one({'id': id}, {'$set': user.to_dict()})
        output = user.to_dict()
    else:
        output = "No such user found"
    return jsonify({'message': output})


# DELETE user by ID
@user_routes.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    user_dict = mongo.db.users.find_one({'id': id})
    if user_dict:
        mongo.db.users.delete_one({'id': id})
        output = "User deleted"
    else:
        output = "No such user found"
    return jsonify({'message': output})