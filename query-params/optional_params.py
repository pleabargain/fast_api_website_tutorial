from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

#uvicorn optional_params:app --reload
# try out any string you like
# http://127.0.0.1:8000/items/334
# http://127.0.0.1:8000/items/dog
# http://127.0.0.1:8000/items/dog_with_a_limp
# http://127.0.0.1:8000/items/hairy%20tree%20frog
