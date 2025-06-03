def test_create_category(client, auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.post("/api/v1/categories/create", json={"name": "Electronics"}, headers=headers)
    assert response.status_code == 200
    assert response.json()["name"] == "Electronics"

def test_list_categories(client):
    response = client.get("/api/v1/categories")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
