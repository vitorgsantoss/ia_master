from langchain import hub
from langchain.prompts import PromptTemplate
from langchain.agents import create_react_agent, AgentExecutor
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_experimental.tools import PythonREPLTool
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model = 'gpt-3.5-turbo')

tools = [DuckDuckGoSearchRun(), PythonREPLTool()]

prompt_template = PromptTemplate.from_template(
    '''
    Como assistente financeiro, reponsável por dar dicas e insights de 
    economia e investimento, responda tudo em português.
    Perguntas: {questions}
    '''
)
questions = '''
    Meu faturamento mensal é de R$3000. Possuo uma dívida fixa de R$815,29 
    relacionada ao financiamento de uma XRE190, minha fatura de cartão de 
    crédito mensal gira em torno de R$2000
    Me dê dicas financeiras
    '''


react_instructions = hub.pull('hwchase17/react')
react_agent = create_react_agent(
    llm = model,
    tools = tools,
    prompt = react_instructions
)
agent_executor = AgentExecutor(
    agent = react_agent,
    tools = tools,
    verbose = True
)
agent_executor.invoke(
    {
        'input': prompt_template.format(questions = questions)
    }
)