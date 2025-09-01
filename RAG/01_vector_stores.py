from dotenv import load_dotenv
from langchain import hub
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

model = ChatOpenAI(model = 'gpt-3.5-turbo')

loader = PyPDFLoader('RAG/laptop_manual.pdf')
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 200
)
chunks = text_splitter.split_documents(
    documents=docs
)

embedding = OpenAIEmbeddings()
vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embedding,
    collection_name = 'laptop_manual'
)
retriever = vector_store.as_retriever()

prompt = hub.pull('rlm/rag-prompt')
rag_chain = (
    {
        'context': retriever,
        'question': RunnablePassthrough()
    }
    | prompt
    | model
    | StrOutputParser()
)

try:
    while True:
        question = input('O que deseja saber?\n')
        response = rag_chain.invoke(question)
        print(response)

except KeyboardInterrupt:
    exit()