import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_purchase_fails_when_quantity_insufficient(auth_headers_user):
    """
    RED TEST:
    Purchasing more sweets than available stock should fail
    with a clear error message.
    """

    # Assume sweet with ID 1 exists and has limited stock
    sweet_id = 1

    response = client.post(
        f"/api/sweets/{sweet_id}/purchase",
        json={"quantity": 999},
        headers=auth_headers_user,
    )

    assert response.status_code == 400
    assert "insufficient" in response.json()["detail"].lower()
