from fastapi import APIRouter, HTTPException, Depends
from fastapi.middleware.throttling import ThrottlingMiddleware
from models import Task, UpdateTaskModel, TaskList
from db import db

tasks_router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
    responses={404: {"description": "Not found"}}
)

@tasks_router.post("/", response_model=Task, status_code=201)  # Created
async def create_task(task: Task):
    try:
        return db.add_task(task)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Database error occurred")


@tasks_router.get("/{task_id}", response_model=Task)
async def get_task(task_id: int):
    if task_id <= 0:
        raise HTTPException(status_code=400, detail="Task ID must be positive")
    task = db.get_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@tasks_router.get("/", response_model=List[Task])
async def get_tasks() -> List[Task]:
    """
    Retrieve all tasks from the database.
    Returns:
        List[Task]: List of all tasks
    """
    return db.get_tasks()


@tasks_router.put("/{task_id}", response_model=Task)
async def update_task(task_id: int, task_update: UpdateTaskModel):
    updated_task = db.update_task(task_id, task_update)
    if updated_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task


@router.delete("/{task_id}")
async def delete_task(task_id: int):
    try:
        db.delete_task(task_id)
        return {"message": f"Task {task_id} deleted successfully"}
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def delete_task(task_id: int):
    db.delete_task(task_id)
    return {"message": "Task deleted successfully"}

@router.delete("/", tags=["danger"])
async def delete_all_tasks():
    """
    Delete all tasks from the database.
    Use with caution!
    """
    db.delete_all_tasks()
    return {"message": "All tasks have been deleted"}
