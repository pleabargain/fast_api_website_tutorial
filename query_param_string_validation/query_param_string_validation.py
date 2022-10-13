# https://fastapi.tiangolo.com/tutorial/query-params-str-validations/

# the URLs start to disappear in the tutorial, so I'm not sure what's going on!

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(q: str | None = None):
# i tride this to see if it works and it doesn't work
# I can't get Foo or Bar to work unless it's an empty /items/ URL

# async def read_items(q: str ):

    results = {"items": [{"item_id": "Foo"}, 
                        {"item_id": "Bar"}]
            }
    if q:
        results.update({"q": q})
    return results

    # to run this
    # uvicorn query_param_string_validation:app --reload

    # this will give all of the objects
    # http://127.0.0.1:8000/items/?
    # so will this
    # http://127.0.0.1:8000/items/?q=Foo
    # and this
    # http://127.0.0.1:8000/items/?q=foo
    
    
        # // 20221013080538
        # // http://127.0.0.1:8000/items/?q=Bar

        # {
        #   "items": [
        #     {
        #       "item_id": "Foo"
        #     },
        #     {
        #       "item_id": "Bar"
        #     }
        #   ],
        #   "q": "Bar"
        # }



    # why? 


    # to test
    # will return all objects
    # http://127.0.0.1:8000/items/
    
    # but this will return 'not found'
    # why!?
    # http://127.0.0.1:8000/items/Foo
    # http://127.0.0.1:8000/items/Bar

    