
def test_unauthorized_access(client):
    res = client.get("/api/sweets")
    assert res.status_code == 401
