from fastapi import FastAPI

from todo import greeting

app = FastAPI()


@app.get("/")
async def root():
    return {"message": greeting()}
