from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

load_dotenv()

model = ChatOpenAI(model = 'gpt-3.5-turbo')

embedding = OpenAIEmbeddings()
vector_store = Chroma(
    collection_name='laptop_manual',
    embedding_function=embedding,
    persist_directory='db'
)
retriever = vector_store.as_retriever()

system_prompt = 'Use o contexto para responder a pergunta.\nContexto: {context}'
prompt = ChatPromptTemplate.from_messages(
    [
        ('system', system_prompt),
        ('human', '{question}')
    ]
)
chain = (
    {
        'context': retriever,
        'question': RunnablePassthrough()
    }
    | prompt
    | model
    | StrOutputParser()
)

question = input('Qual a sua dúvida?\n')
response = chain.invoke(question)
print(response)