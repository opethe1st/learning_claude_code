"""Tests for FastAPI endpoints."""

from fastapi.testclient import TestClient


def test_read_root(client: TestClient) -> None:
    """Test root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Learning Claude Code API"
    assert data["version"] == "0.1.0"
    assert data["docs"] == "/docs"


def test_health_check(client: TestClient) -> None:
    """Test health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_list_items_empty(client: TestClient) -> None:
    """Test listing items when database is empty."""
    response = client.get("/api/items")
    assert response.status_code == 200
    assert response.json() == []


def test_create_item(client: TestClient) -> None:
    """Test creating a new item."""
    item_data = {
        "name": "Test Item",
        "description": "A test item",
        "price": 9.99,
        "quantity": 10,
    }
    response = client.post("/api/items", json=item_data)
    assert response.status_code == 201
    data = response.json()
    assert data["message"] == "Item created successfully"
    assert data["item"]["name"] == "Test Item"
    assert data["item"]["price"] == 9.99
    assert "id" in data["item"]


def test_get_item(client: TestClient) -> None:
    """Test getting a specific item."""
    # First create an item
    item_data = {
        "name": "Get Test Item",
        "description": "Item for get test",
        "price": 19.99,
        "quantity": 5,
    }
    create_response = client.post("/api/items", json=item_data)
    item_id = create_response.json()["item"]["id"]

    # Now get the item
    response = client.get(f"/api/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == item_id
    assert data["name"] == "Get Test Item"
    assert data["price"] == 19.99


def test_get_item_not_found(client: TestClient) -> None:
    """Test getting a non-existent item."""
    response = client.get("/api/items/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"


def test_update_item(client: TestClient) -> None:
    """Test updating an item."""
    # First create an item
    item_data = {
        "name": "Update Test Item",
        "description": "Item to update",
        "price": 29.99,
        "quantity": 15,
    }
    create_response = client.post("/api/items", json=item_data)
    item_id = create_response.json()["item"]["id"]

    # Update the item
    updated_data = {
        "name": "Updated Item",
        "description": "Updated description",
        "price": 39.99,
        "quantity": 20,
    }
    response = client.put(f"/api/items/{item_id}", json=updated_data)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == item_id
    assert data["name"] == "Updated Item"
    assert data["price"] == 39.99


def test_update_item_not_found(client: TestClient) -> None:
    """Test updating a non-existent item."""
    item_data = {
        "name": "Test",
        "description": "Test",
        "price": 10.0,
        "quantity": 1,
    }
    response = client.put("/api/items/99999", json=item_data)
    assert response.status_code == 404


def test_delete_item(client: TestClient) -> None:
    """Test deleting an item."""
    # First create an item
    item_data = {
        "name": "Delete Test Item",
        "description": "Item to delete",
        "price": 49.99,
        "quantity": 25,
    }
    create_response = client.post("/api/items", json=item_data)
    item_id = create_response.json()["item"]["id"]

    # Delete the item
    response = client.delete(f"/api/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Item deleted successfully"

    # Verify it's deleted
    get_response = client.get(f"/api/items/{item_id}")
    assert get_response.status_code == 404


def test_delete_item_not_found(client: TestClient) -> None:
    """Test deleting a non-existent item."""
    response = client.delete("/api/items/99999")
    assert response.status_code == 404


def test_create_item_validation(client: TestClient) -> None:
    """Test item creation with invalid data."""
    # Test with negative price
    invalid_item = {
        "name": "Invalid Item",
        "description": "Has negative price",
        "price": -10.0,
        "quantity": 5,
    }
    response = client.post("/api/items", json=invalid_item)
    assert response.status_code == 422  # Unprocessable Entity

    # Test with empty name
    invalid_item2 = {
        "name": "",
        "description": "Empty name",
        "price": 10.0,
        "quantity": 5,
    }
    response = client.post("/api/items", json=invalid_item2)
    assert response.status_code == 422
