from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate
from langchain_core.messages import AIMessage, HumanMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chat_prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template('Você é um agente especializado em {specialization}')
    ]
)

model = ChatOpenAI(model = 'gpt-3.5-turbo')

prompt = chat_prompt.format_messages(
    specialization = input('Informe a área de especialização: ')
)

while True:
    prompt.append(
        HumanMessage(input('Digite abaixo o que deseja falar ao GPT: '))
    )
    response = model.invoke(prompt)
    print(response.content)

    prompt.append(
        AIMessage(response.content)
    )
    print(prompt)