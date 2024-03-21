from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_from_decimal_to_binary_converter():
    response = client.put("/converter?decimal=29")
    assert response.status_code == 200
    assert response.json() == 11101

    response = client.put("/converter?decimal=1")
    assert response.status_code == 200
    assert response.json() == 1

    response = client.put("/converter?decimal=0")
    assert response.status_code == 200
    assert response.json() == 0

def test_from_binary_to_decimal_converter():
    response = client.put("/converter?bin=11101")
    assert response.status_code == 200
    assert response.json() == 29

    response = client.put("/converter?bin=1")
    assert response.status_code == 200
    assert response.json() == 1

    response = client.put("/converter?bin=0")
    assert response.status_code == 200
    assert response.json() == 0