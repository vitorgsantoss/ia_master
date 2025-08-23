from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model = 'gpt-3.5-turbo'
)

messages = [
    {'role': 'system', 'content': 'Você é um especialista em homologações de veículos seguindo as normas do Proconve'},
    {'role': 'user', 'content': 'Me explique como se calcula a emissão de aldeídos em um teste de veículo'}
]

response = model.invoke(messages)

print(response)
print(response.content)