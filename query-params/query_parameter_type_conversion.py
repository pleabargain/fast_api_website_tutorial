from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

# https://fastapi.tiangolo.com/tutorial/query-params/


# run server
# uvicorn query_parameter_type_conversion:app --reload   

#test

# true value print out just the first string
# http://127.0.0.1:8000/items/silly?short=on
# http://127.0.0.1:8000/items/fantastic?short=on
# http://127.0.0.1:8000/items/foo?short=1


# false value will print out long string
# http://127.0.0.1:8000/items/foo?short=False
# http://127.0.0.1:8000/items/foo?short=off
# http://127.0.0.1:8000/items/foo?short=0