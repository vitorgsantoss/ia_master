from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model = 'gpt-3.5-turbo')
prompt = PromptTemplate.from_template(
    '''
    Você é um agente que receberá um contexto e uma pergunta, responda as
    perguntas apenas com base no contexto, evite fazer buscas externas.
    Contexto: {context}.
    Pergunta: {question}.
    '''
)
chain = prompt | model | StrOutputParser()

# Teste com arquivo txt
# loader = TextLoader('teste.txt')
# documents = loader.load()

# Teste com arquivo pdf
loader = PyPDFLoader('teste.pdf')
documents = loader.load()

response = chain.invoke(
    {
        'context': '\n'.join([doc.page_content for doc in documents]),
        'question': 'Qual o alimento mais rico em nutrientes da lista?'
    }
)
print(response)