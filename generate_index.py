import os
import logging
import sys

import llama_index as llama

def main():
    print("embedding作成処理開始")
    print("環境設定")
    os.environ["OPENAI_API_KEY"] = "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"
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, force=True)

    # インデックスの作成
    print("インデックス作成")
    documents = llama.SimpleDirectoryReader("data").load_data()
    index = llama.GPTVectorStoreIndex.from_documents(documents)

    print("インデックス保存")
    index.storage_context.persist()

    print("試しに使用")
    query_engine = index.as_query_engine()
    print(query_engine.query("ぼっちちゃんの得意な楽器は？"))

if __name__ == "__main__":
    main()