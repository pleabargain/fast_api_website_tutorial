from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# to run it
# uvicorn main:app --reload
# if you get "ERROR:    Error loading ASGI app. Could not import module "main"."
# make sure you are in the correct directory in the terminal
# check out the docs: http://127.0.0.1:8000/docs
# check this out: http://127.0.0.1:8000/openapi.json
