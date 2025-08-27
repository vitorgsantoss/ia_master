from langchain_experimental.tools import PythonREPLTool
from langchain_experimental.agents.agent_toolkits import create_python_agent
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model = 'gpt-3.5-turbo')
python_repl_tool = PythonREPLTool()
agent = create_python_agent(
    llm = model,
    tool = python_repl_tool,
    verbose = True
)
prompt = PromptTemplate.from_template(
    'Resolva o problema: {problem}'
)
prompt = prompt.format(problem = 'Qual a raiz cúbica de 27')
agent.invoke(prompt)