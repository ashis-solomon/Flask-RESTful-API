from flask import abort
from flask_restful import Resource, marshal_with, fields, reqparse
from bson import ObjectId

from db import users_collection


user_parser = reqparse.RequestParser()
user_parser.add_argument('name', type=str, required=True)
user_parser.add_argument('email', type=str, required=True)
user_parser.add_argument('password', type=str, required=True)

user_fields = {
    '_id': fields.String(attribute=lambda x: str(x['_id'])),
    'name': fields.String,
    'email': fields.String,
    'password': fields.String
}

class User(Resource):
    @marshal_with(user_fields)
    def get(self, id=None):
        if id:
            user = users_collection.find_one({'_id': ObjectId(id)})
            if user:
                return user
            else:
                abort(404, error='User not found')
        else:
            users = users_collection.find()
            return [user for user in users]

    @marshal_with(user_fields)
    def post(self):
        args = user_parser.parse_args()
        result = users_collection.insert_one(args)
        user = users_collection.find_one({'_id': result.inserted_id})
        return user, 201

    @marshal_with(user_fields)
    def put(self, id):
        args = user_parser.parse_args()
        result = users_collection.update_one({'_id': ObjectId(id)}, {'$set': args})
        if result.matched_count == 1:
            user = users_collection.find_one({'_id': ObjectId(id)})
            return user, 200
        else:
            abort(404, error='User not found')

    def delete(self, id):
        result = users_collection.delete_one({'_id': ObjectId(id)})
        if result.deleted_count == 1:
            return {'message': 'User deleted successfully'}, 200
        else:
            abort(404, error='User not found')
