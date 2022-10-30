import os

from fastapi import FastAPI

app = FastAPI()

password = os.environ.get('TEST_SERVER_DB_PASSWORD')


@app.get("/")
async def get_all_students():
    return password
