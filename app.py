from flask import Flask, request, abort
from flask_restful import Api

from resources.users import User


app = Flask(__name__)
api = Api(app)


api.add_resource(User, '/users', '/users/<id>')

if __name__ == '__main__':
    app.run(debug=True)
