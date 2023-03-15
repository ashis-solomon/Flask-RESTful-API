import requests, random, string
from config import Config

ENDPOINT = Config.BASE_URL



random_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
payload = {
    "name": random_name,
    "email": f"{random_name}@xyz.com",
    "password": f"password_{random_name}"
}

# helper function definitions

# check for payload similarity with response
def check_json(resp, payload):
    for key in payload:
        if resp[key] != payload[key]:
            return False
    return True

def get_specific_user(id):
    return requests.get(ENDPOINT + f'/users/{id}')

def get_users(payload):
    return requests.get(ENDPOINT)

def create_user(payload):
    return requests.post(ENDPOINT + '/users', json=payload)

def update_user(id):
    return requests.put(ENDPOINT + f'/users/{id}')


# -------------------------------------------------------------------


def test_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200


def test_get_users():
    response = get_users(payload)
    assert 'message' in response.json()


def test_get_specific_user():
    response = create_user(payload)
    resp_id = None

    if 'message' in response.json():
        resp_id = response.json()['message']['id']
        resp = get_specific_user(resp_id)
        assert 'message' in resp.json()
    else:
        assert 'error' in response.json()
    
    assert 'message' in requests.delete(ENDPOINT + f'/users/{resp_id}').json()


def test_create_delete_user():
    
    response = create_user(payload)

    if 'message' in response.json():
        assert check_json(response.json()['message'], payload), "JSON response does not match expected payload"
        resp_id = response.json()['message']['id']
        response = requests.delete(ENDPOINT + f'/users/{resp_id}')
        assert response.json()['message'] == 'User deleted'
    else:
        assert response.json()['error'] == 'User with this email already exists'


def test_update_user():
    response = create_user(payload)
    resp_id = None

    if response.status_code == 200 and 'message' in response.json():
        resp_id = response.json()['message']['id']
        resp = update_user(resp_id)
        if resp.headers['Content-Type'] == 'application/json':
            assert 'message' in resp.json()
            assert check_json(resp.json()['message'], payload), "JSON response does not match expected payload"
        else:
            assert resp.status_code == 400
    else:
        assert response.status_code == 400
    
    assert 'message' in requests.delete(ENDPOINT + f'/users/{resp_id}').json()