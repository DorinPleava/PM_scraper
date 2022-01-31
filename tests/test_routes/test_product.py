import json


def test_create_user(client):
    data = {
  "id": 0,
  "name": "string",
  "type": "string",
  "pieces": 0,
  "in_stock": True,
  "total_price": 0,
  "url": "string"
}
    response = client.get("/docs")
    print(response)
    assert response.status_code == 200 
    assert response.json()["email"] == "testuser@nofoobar.com"
    # assert response.json()["is_active"] == Tru