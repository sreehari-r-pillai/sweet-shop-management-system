
def login(client, user, pwd):
    return client.post("/api/auth/login", json={"username": user, "password": pwd}).json()["access_token"]

def test_admin_only_add_sweet(client):
    token = login(client, "admin", "admin")
    res = client.post("/api/sweets",
        headers={"Authorization": f"Bearer {token}"},
        json={"name": "Barfi", "category": "Indian", "price": 20, "quantity": 10}
    )
    assert res.status_code == 200

def test_user_forbidden_add_sweet(client):
    token = login(client, "user1", "pass")
    res = client.post("/api/sweets",
        headers={"Authorization": f"Bearer {token}"},
        json={"name": "Halwa", "category": "Indian", "price": 15, "quantity": 5}
    )
    assert res.status_code == 403
