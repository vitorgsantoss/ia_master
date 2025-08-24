from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-3.5-turbo')

runnable_sequency = (
    PromptTemplate.from_template(
        'Me diga que são os principais Anti-heróis do universo {universe}'
    )
    | model
    | StrOutputParser()
)

response = runnable_sequency.invoke({'universe': 'Marvel'})

print(response)