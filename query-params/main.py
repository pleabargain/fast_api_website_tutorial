from fastapi import FastAPI

app = FastAPI()
# created some fake data on https://www.mockaroo.com/
fake_items_db = [
                {
  "item_name": "frame"
}, {
  "item_name": "composite"
}, {
  "item_name": "impactful"
}, {
  "item_name": "database"
}, {
  "item_name": "scalable"
}, {
  "item_name": "success"
}, {
  "item_name": "logistical"
}, {
  "item_name": "context-sensitive"
}, {
  "item_name": "open system"
}, {
  "item_name": "firmware"
}, {
  "item_name": "firmware"
}, {
  "item_name": "project"
}, {
  "item_name": "matrix"
}, {
  "item_name": "clear-thinking"
}, {
  "item_name": "Reverse-engineered"
}, {
  "item_name": "Centralized"
}, {
  "item_name": "Graphic Interface"
}, {
  "item_name": "middleware"
}, {
  "item_name": "Innovative"
}, {
  "item_name": "systemic"
},
    
                {"item_name": "Foo"}, 
                {"item_name": "Bar"}, 
                {"item_name": "Baz"},
                {  "item_name": "Sportvan G30"
                }, {
                "item_name": "SLX"
                }, {
                "item_name": "Celica"
                }, {
                "item_name": "TL"
                }, {
                "item_name": "S80"
                }]
                
                
@app.get("/items/")
# declare as python type: int 
# default query start at 0 and show only 10 items
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

    # try it out http://127.0.0.1:8000/items/?skip=0&limit=10
    # this will skip over the first  and limit to 8
    # http://127.0.0.1:8000/items/?skip=3&limit=8
    # this will return no items because it is out of range of the data but it doesn't throw an error!
    # http://127.0.0.1:8000/items/?skip=50