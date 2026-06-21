import uuid

from fastapi import FastAPI

app = FastAPI(
    title="UUID Generator API",
    description="Generate random UUID's",
    version="1.0"
)

@app.get("/")
def home():
    return {
        "message" : "Welcome to UUID Generator API"
    }

@app.get("/uuid")
def generate_uuid():
    return {
        "uuid" : str(uuid.uuid4())
    }

@app.get("/uuids{count}")
def generate_multiple_uuids(count:int):
    ids=[str(uuid.uuid4()) for _ in range(count)]

    return {
        "count" : count,
        "ids" : ids
    }

@app.get("/uuid/{version}")
def generate_uuid_by_version(version : int):

    if version == 1:
        generated_uuid = uuid.uuid1()

    elif version == 4:
        generated_uuid = uuid.uuid4()


    else:
        return {
            "error" : "Only UUID 1 and 4 version are supported"
        }


    return {
        "version" : version,
        "uuid" : str(generated_uuid)
    }
