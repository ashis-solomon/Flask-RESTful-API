from flask import Flask
from routes.routes import *

app = Flask(__name__)
app.register_blueprint(user_routes)


if __name__ == '__main__':
    app.run(debug=True)