from langchain_community.vectorstores import FAISS
from langchain_community.vectorstores.utils import DistanceStrategy

from mylangchain.langchain_embedder import Embedder
from mylangchain.langchain_rag_maker import LangchainRagMaker
from mylangchain.langchain_requester import LangchainRequester

embedder = Embedder("http://localhost:5000/v1")
documents_arr = LangchainRagMaker().load()

vectorstore = None
for documents in documents_arr:
    temp_store = FAISS.from_documents(
            documents=documents,
            embedding=embedder,
            distance_strategy=DistanceStrategy.COSINE
        )
    if vectorstore is not None:
        vectorstore.merge_from(temp_store)
    else:
        vectorstore = temp_store

chain = LangchainRequester.ready(vectorstore=vectorstore)

while True:
    question = input("질문을 입력, 그냥 엔터치면 종료: ")
    if len(question) == 0:
        break
    LangchainRequester.chat(chain, question)
