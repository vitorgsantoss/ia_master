from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model = 'gpt-3.5-turbo')

runnable_chain = (
    PromptTemplate.from_template(
        'Me informe quem foi {historical_character}'
    )
    | model
    | StrOutputParser()
)

response = runnable_chain.invoke({'historical_character': 'Albert Einstein'})
print(response)