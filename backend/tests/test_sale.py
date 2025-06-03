def test_create_sale(client, auth_token):
    from datetime import datetime

    headers = {"Authorization": f"Bearer {auth_token}"}

    # create a new category
    response = client.post("/api/v1/categories/create", json={"name": "Kitchen"}, headers=headers)
    category_data = response.json()

    # create a new product
    response = client.post("/api/v1/products/create", json={
        "description": "Stove",
        "price": 599.90,
        "category_id": category_data["id"],
        "stock_quantity": 10,
    }, headers=headers)
    product_data = response.json()

    # create a buyer user
    response = client.post("/api/v1/auth/register", json={
        "username": "buyer.user",
        "name": "Buyer",
        "last_name": "User",
        "email": "buyer.user@example.com",
        "password": "123456"
    })
    buyer_data = response.json()

    # create a sale
    response = client.post("/api/v1/sales/create", json={
        "product_id": product_data["id"],
        "buyer_id": buyer_data["id"],
        "seller_id": 1,
        "quantity": 9,
        "sale_price": product_data["price"],
        "timestamp": str(datetime.utcnow())
    }, headers=headers)

    assert response.status_code == 200
    data = response.json()
    assert data["product_id"] == product_data["id"]
    assert data["buyer_id"] == buyer_data["id"]

def test_get_sales(client):
    response = client.get("/api/v1/sales")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
