from fastapi import FastAPI

from todo.routes.api.v1.todos import todos
from todo import greeting

app = FastAPI()
app.include_router(todos, prefix="/api/v1", tags=["api"])


@app.get("/")
async def root():
    return {"message": greeting()}
