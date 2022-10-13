from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
    

app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    # what is the URL for this one?
    # check the docs http://127.0.0.1:8000/docs#/default/get_model_models__model_name__get
    # and run lenet
    # http://127.0.0.1:8000/models/lenet


    # since resnet is not defined, it will return the default message
    return {"model_name": model_name, "message": "Have some residuals"}
    # start the server and try it out: http://127.0.0.1:8000/models/resnet


# run
# uvicorn testing_enum:app --reload