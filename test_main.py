from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

data = {
  "recipe_name": "Potato with Tomato",
  "time_to_cooking": 30,
  "ingredients": "potato, tomato",
  "description": "use potato and tomate"
}

def test_post_data():
    response = client.post("/recipes", json=data)
    assert response.status_code == 200

def test_get_data():
    response = client.get("/recipes")
    assert response.status_code == 200
    assert response.json() == [{"recipe_name": "Potato with Tomato",  "time_to_cooking": 30, 'views': 0}]

def test_get_id():
    response = client.get("/recipes/1")
    assert response.status_code == 200
    assert response.json() == {"ingredients": "potato, tomato", "description": "use potato and tomate"}



