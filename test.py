import requests
from config import Config

ENDPOINT = Config.BASE_URL



def test_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200