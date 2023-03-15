# Corider - Hiring Assignment

## Flask Application for CRUD operations on MongoDB

version: 1.0.0

`server`: localhost:5000


## Requirements
The application is developed using the following:

- Flask
- PyMongo


The User resource has the following fields:

- id (a unique identifier for the user)
- name (the name of the user)
- email (the email address of the user)
- password (the password of the user)
</br></br>
## Installation
1. Clone the repository.
2. Install the dependencies from requirements.txt.</br><br>
    `
        pip install -r requirements.txt
    `
    <br><br>
3. Activate the virtual environment</br><br>
    `
        source env/bin/activate
    `
    <br><br>
3. Set the MongoDB URI and database name in the Flask application configuration in `config.py`.<br><br>
`
DB_NAME = 'db'
    MONGODB_URI = os.environ.get('MONGODB_URI') or 'mongodb://localhost:27017/db'
`
<br><br>
4. Run the Flask application using the command `flask run`.
</br></br>
## Usage
Run the Flask application using the command `flask run`.
Use Postman to test the REST API endpoints.
</br></br>
## Endpoints
The application provides REST API endpoints for CRUD operations on a User resource:
</br></br>
## GET /users
`
Sample Response: </br>
{
    "result": [
        {
            "id": "298a8d10-96ac-48f1-827f-82a1d2f0b3be",
            "name": "John",
            "email": "john@example.com",
            "password": "password1"
        },
        {
            "id": "19def540-89db-4d7a-b1d2-ee72abf86843",
            "name": "Jane",
            "email": "jane@example.com",
            "password": "password2"
        }
    ]
}
`
</br></br>
## GET /users<id> 
Request: GET /users/298a8d10-96ac-48f1-827f-82a1d2f0b3be
Sample Response: </br>

`
{
    "result": {
        "id": "298a8d10-96ac-48f1-827f-82a1d2f0b3be",
        "name": "John",
        "email": "john@example.com",
        "password": "password1"
    }
}
`
</br></br>
## POST /users
Content-Type: application/json</br>
`
{
    "name": "Mike",
    "email": "mike@example.com",
    "password": "password3"
}
`
Sample Response:</br>
`
{
    "result": {
        "id": "91bf295c-4f50-45c1-bfee-a96fcb5a64a4",
        "name": "Mike",
        "email": "mike@example.com",
        "password": "password3"
    }
}
`
</br></br>
## PUT /users/id
Request: PUT /users/298a8d10-96ac-48f1-827f-82a1d2f0b3be
Content-Type: application/json</br>
`
{
    "name": "John Smith",
    "email": "johnsmith@example.com",
    "password": "password4"
}
`

Sample Response:</br>
`
{
    "result": {
        "id": 1,
        "name": "John Smith",
        "email": "johnsmith@example.com",
        "password": "password4"
    }
}
`
</br></br>
## DELETE /users<id> 
Request: DELETE /users/298a8d10-96ac-48f1-827f-82a1d2f0b3be
Sample Response: </br>
`
{
    "result": "User deleted"
}
`