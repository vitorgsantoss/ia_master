from langchain_community.tools import WikipediaQueryRun
from langchain.utilities import WikipediaAPIWrapper
from langchain_experimental.agents.agent_toolkits import create_python_agent
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model = 'gpt-3.5-turbo')

wikipedia_tool = WikipediaQueryRun(
    api_wrapper = WikipediaAPIWrapper(
        lang = 'pt'
    )
)
agent_executor = create_python_agent(
    llm = model,
    tool = wikipedia_tool, 
    verbose = True
)
prompt = PromptTemplate.from_template(
    '''
    Faça uma busca na web por {query}, e dê a resposta em português brasileiro
    '''
)
prompt = prompt.format(query = 'DC Pacificador')

agent_executor.invoke(prompt)