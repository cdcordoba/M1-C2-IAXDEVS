from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_task():
    response = client.post(
        "/tasks/",
        json={"title": "Integration Test", "description": "Test", "completed": False}
    )
    assert response.status_code == 201
    assert response.json()["title"] == "Integration Test"

def test_get_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_delete_task():
    # Create a task first
    task = client.post(
        "/tasks/",
        json={"title": "Delete Test", "description": "Test", "completed": False}
    ).json()
    
    # Then delete it
    response = client.delete(f"/tasks/{task['id']}")
    assert response.status_code == 200