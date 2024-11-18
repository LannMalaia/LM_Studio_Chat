from langchain_openai import ChatOpenAI
from langchain_core.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.memory import ConversationBufferMemory
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain

class LangchainRequester:
    def ready(vectorstore):

        # 언어 모델
        llm = ChatOpenAI(
            base_url="http://localhost:5000/v1",
            api_key="lm-studio",
            model="aya-expanse-8b",
            temperature=0.8,
            streaming=True,
            max_tokens=300,
            callbacks=[StreamingStdOutCallbackHandler()] # 스트림시 출력되는 콜백 함수
        )

        # 메모리
        memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )

        # RAG 체인
        chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=vectorstore.as_retriever(search_kwargs={"k":3}),
            memory=memory,
            return_source_documents=True,
            combine_docs_chain_kwargs={
                "prompt": ChatPromptTemplate.from_messages([
                    ("system", """
                     200단어가 넘지 않게 짧고 간결하게 대답해줘.
                     모든 문장은 한국어로 표현해.
                     아래에 문서 내용이 있을 경우, 최대한 문서 내용을 기반으로 답해줘.
                     
                     문서 내용: {question}
                     """),
                    ("user", "{context}")
                ])
            }
        )

        return chain
    
    def chat(chain, question):
        try:
            response = chain({"question": question})
            sources = [doc.metadata.get('source', 'Unknown') for doc in response['source_documents']]
            return response['answer'], sources
        except Exception as e:
            print("대화 중 오류 발생")
            print(e)
            return None, None

