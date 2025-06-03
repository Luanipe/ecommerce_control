def test_create_product(client, auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.post("/api/v1/categories/create", json={"name": "Books"}, headers=headers)
    category_data = response.json()

    response = client.post("/api/v1/products/create", json={
        "description": "Test Book",
        "price": 39.90,
        "category_id": category_data.get("id"),
        "stock_quantity": 10,
    }, headers=headers)

    assert response.status_code == 200
    data = response.json()
    assert data["description"] == "Test Book"
    assert data["stock_quantity"] == 10

def test_list_products(client):
    response = client.get("/api/v1/products")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
