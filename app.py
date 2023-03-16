from flask import Flask, request
from flask_restful import Resource, Api
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
api = Api(app)

client = MongoClient('mongodb://localhost:27017/')
db = client['db']
users_collection = db['users_db']

class User(Resource):
    def get(self, id=None):
        if id:
            user = users_collection.find_one({'_id': ObjectId(id)})
            if user:
                user['_id'] = str(user['_id'])
                return user
            else:
                return {'error': 'User not found'}, 404
        else:
            users = []
            for user in users_collection.find():
                user['_id'] = str(user['_id'])
                users.append(user)
            return users

    def post(self):
        data = request.json
        result = users_collection.insert_one(data)
        user_id = str(result.inserted_id)
        return {'id': user_id}, 201

    def put(self, id):
        data = request.json
        result = users_collection.update_one({'_id': ObjectId(id)}, {'$set': data})
        if result.matched_count == 1:
            return {'message': 'User updated successfully'}, 200
        else:
            return {'error': 'User not found'}, 404

    def delete(self, id):
        result = users_collection.delete_one({'_id': ObjectId(id)})
        if result.deleted_count == 1:
            return {'message': 'User deleted successfully'}, 200
        else:
            return {'error': 'User not found'}, 404


api.add_resource(User, '/users', '/users/<id>')

if __name__ == '__main__':
    app.run(debug=True)
