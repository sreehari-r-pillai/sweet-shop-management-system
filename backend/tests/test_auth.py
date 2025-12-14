
def test_register_user(client):
    res = client.post("/api/auth/register", json={"username": "user1", "password": "pass"})
    assert res.status_code == 200

def test_register_admin(client):
    res = client.post("/api/auth/register", json={"username": "admin", "password": "admin", "role": "ADMIN"})
    assert res.status_code == 200

def test_login(client):
    res = client.post("/api/auth/login", json={"username": "admin", "password": "admin"})
    assert "access_token" in res.json()
