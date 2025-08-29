from dotenv import load_dotenv
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model = 'gpt-4-turbo')

db = SQLDatabase.from_uri('sqlite:///agents/empresa.db')
toolkit = SQLDatabaseToolkit(
    db = db,
    llm = model
)
system_message = hub.pull('hwchase17/react')
db_agent = create_react_agent(
    llm = model,
    tools = toolkit.get_tools(),
    prompt = system_message
)
db_agent_executor = AgentExecutor(
    agent = db_agent,
    tools = toolkit.get_tools(),
    verbose = True
)

prompt = PromptTemplate.from_template(
    '''
    Use as ferrmentas necessárias para responder perguntas relacionadas ao 
    banco de dados de funcionário da minha empresa.
    Responda tudo em português brasileiro.
    Perguntas: {question}
    '''
)
question = '''Baseado nos dados, qual é o meu funcionário mais antigo?
'''

db_agent_executor.invoke(
    {
        'input': prompt.format(question = question)
    }
)