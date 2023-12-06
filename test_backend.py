from backend import app
from fastapi.testclient import TestClient

test_client = TestClient(app)


def test_make_prediction():
    response = test_client.post("/predict", json = {"year" : "2021", "month" : "01"})
    assert response.status_code == 200
    assert response.json() == {"prediction" : "22.0"}