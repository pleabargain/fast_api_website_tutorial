# the tutorial loses coherence here https://fastapi.tiangolo.com/tutorial/body/
# the tutorial is not clear 

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    
    return item

# nothing is found
# http://127.0.0.1:8000/items/foo
# http://127.0.0.1:8000/items/1

# check out the docs
# http://127.0.0.1:8000/docs#/default/create_item_items__post