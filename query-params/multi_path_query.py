# Multiple path and query parameters
# https://fastapi.tiangolo.com/tutorial/query-params/

from fastapi import FastAPI

app = FastAPI()


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, 
    item_id: str, 
    q: str | None = None, 
    short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "note \n does not appear to generate line breaks. This is an amazing item that has a long description because the short parameter is set to \nFalse or \noff or \n0"}
        )
    return item

# run server
# uvicorn multi_path_query:app --reload
# try it out
 # http://127.0.0.1:8000/users/1/items/silly?short=on

  # http://127.0.0.1:8000/users/1/items/silly?short=off