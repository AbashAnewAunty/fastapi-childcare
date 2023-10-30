from fastapi import FastAPI
from llama_index import StorageContext, load_index_from_storage

app = FastAPI()

@app.get("/")
def index():
    return {"Hello": "World"}

@app.get("/query/{query}")
async def answer_with_llamaindex(text: str):
    # インデックスの読み込み
    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    index = load_index_from_storage(storage_context)
    query_engine = index.as_query_engine()
    answer = query_engine.query("質問：{query}")
    return {"Answer": f"{answer.response}"}