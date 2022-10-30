import os

from fastapi import FastAPI

app = FastAPI()


print(os.environ.get('TEST_SERVER_DB_PASSWORD'))
print(os.environ.get('TEST_SERVER_HOST'))


@app.get("/")
async def get_all_students():
    return {"Hello world"}
