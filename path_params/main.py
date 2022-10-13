from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
# check it out http://127.0.0.1:8000/items/foo

# check it out http://127.0.0.1:8000/items/3

# http://127.0.0.1:8000/items/foo
# docs say: http://127.0.0.1:8000/docs
