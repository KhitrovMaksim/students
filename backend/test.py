from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def get_all_students():
    return {"Hello world"}
