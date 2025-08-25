from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model = 'gpt-3.5-turbo')

classification_agent = (
    PromptTemplate.from_template(
        '''
        Você é um agente responsável por filtrar a pergunta do usuário e 
        retornar se corresponde a uma dúvida relacionada ao setor financeiro,
        suporte técnico ou outras informações.
        Pergunta: {question}
        '''
    )
    | model
    | StrOutputParser()
)

financial_agent = (
    PromptTemplate.from_template(
        '''
        Você é um agente reponsável por sanar dúvidas do usuário quanto ao setor 
        financeiro, comece suas conversas com:
        Bem-vindo ao setor financeiro...
        E a seguir trabalhe na solução da pergunta do usuário, pergunta:
        {question}
        '''
    )
    | model
    | StrOutputParser()
)

tech_support_agent = (
    PromptTemplate.from_template(
        '''
        Você é um agente reponsável por sanar dúvidas do usuário quanto ao setor 
        de suporte técnico, comece suas conversas com:
        Bem-vindo ao setor de suporte técnico...
        E a seguir trabalhe na solução da pergunta do usuário, pergunta:
        {question}
        '''
    )
    | model
    | StrOutputParser()
)

other_info_agent = (
    PromptTemplate.from_template(
        '''
        Você é um agente reponsável por sanar dúvidas do usuário quanto ao setor 
        de outras informações, comece suas conversas com:
        Bem-vindo ao setor de outras informações...
        E a seguir trabalhe na solução da pergunta do usuário, pergunta:
        {question}
        '''
    )
    | model
    | StrOutputParser()
)


def route(classification):
    classification = classification.lower()
    if 'financeiro' in classification:
        return financial_agent
    
    elif 'suporte' in classification:
        return tech_support_agent
    
    return other_info_agent


if __name__ == '__main__':
    question = input('Informe sua pergunta: ')
    classification = classification_agent.invoke({'question': question})

    agent = route(classification)
    response = agent.invoke({'question': question})

    print(response)