from apistar import test

from app import app, cars

client = test.TestClient(app)


def test_list_cars():
    response = client.get('/')
    assert response.status_code == 200
    cars = response.json()
    assert type(cars) == list
    assert len(cars) == 1000
    car = cars[0]
    assert car == {"id": 1, "manufacturer": "Audi", "model": "S4", "year": 2005, "vin": "WVWED7AJ9CW312992"}
    assert cars[-1] == {"id": 1000, "manufacturer": "Cadillac", "model": "Escalade", "year": 2009,
                        "vin": "WAUYGAFC3CN434486"}
