import pytest
from db import db

def test_add_task():
    task = {"title": "Test Task", "description": "Test Description", "completed": False}
    result = db.add_task(task)
    assert result["title"] == task["title"]
    assert "id" in result

def test_get_task():
    task = db.add_task({"title": "Get Test", "description": "Test", "completed": False})
    result = db.get_task(task["id"])
    assert result["id"] == task["id"]

def test_delete_task():
    task = db.add_task({"title": "Delete Test", "description": "Test", "completed": False})
    db.delete_task(task["id"])
    with pytest.raises(Exception):
        db.get_task(task["id"])