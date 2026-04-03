from fastapi import APIRouter

import todo

todos = APIRouter(prefix="/todos", tags=["todos"])

@todos.post("/")
def add_todo(description: str) -> dict:
    return {
        "id": 1, 
        "description": description, 
        "completed": False
    }


@todos.put("/{todo_id}")
def complete_todo(todo_id: int) -> dict:
    return {
        "id": todo_id, 
        "description": "Example", 
        "completed": True
    }

@todos.delete("/{todo_id}")
def delete_todo(todo_id: int) -> dict:
    return {
        "id": todo_id, 
        "description": "Example", 
        "completed": False
    }

@todos.get("/active")
def active_todos() -> list:
    return [
        {"id": 1, "description": "Example 1", "completed": False},
        {"id": 2, "description": "Example 2", "completed": False}
    ]

@todos.get("/completed")
def completed_todos() -> list:
    return [
        {"id": 3, "description": "Example 3", "completed": True},
        {"id": 4, "description": "Example 4", "completed": True}
    ]
