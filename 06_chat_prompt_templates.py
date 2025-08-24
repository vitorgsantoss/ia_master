from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chat_template = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template('Você é um agente especializado em {specialization}'),
    ]
)
print('Informe a área de especialização: ')
prompt = chat_template.format_messages(
    specialization = input()
)

model = ChatOpenAI(
    model = 'gpt-3.5-turbo', 
)

while True:
    print('Digite sua mensagem: ')
    message = HumanMessage(
        input()
    )
    prompt.append(message) 

    response = model.invoke(prompt)
    print(response.content)

    prompt.append(AIMessage(response.content))

    print(prompt)