from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model = 'gpt-3.5-turbo')

db = SQLDatabase.from_uri('sqlite:///ipca.db')
toolkit = SQLDatabaseToolkit(
    db = db,
    llm = model
)

system_instructions = hub.pull('hwchase17/react')
db_agent = create_react_agent(
    llm = model,
    tools = toolkit.get_tools(),
    prompt = system_instructions
)
db_agent_executor = AgentExecutor(
    agent = db_agent,
    tools = toolkit.get_tools(),
    verbose = True
)

prompt = PromptTemplate.from_template(
    '''
    Use as ferrmentas necessárias para responder perguntas relacionadas ao histórico de IPCA ao longo dos anos.
    Responda tudo em português brasileiro.
    Perguntas: {q}
    '''
)
question = 'Qual a maior taxa de ipca registrada no banco de dados?'
db_agent_executor.invoke(
    {
        'input': prompt.format(q = question)
    }
)