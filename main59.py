from fastapi import FastAPI

app = FastAPI()


@app.post("/items/", status_code=201)
async def create_items(name: str):
    return {"name": name}
