from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"Hello": "World"}

@app.get("/query/{text}")
async def index2(text: str):
    return {"Hello": f"World I am {text}"}
