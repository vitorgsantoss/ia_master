from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv('.env')

model = OpenAI()
response = model.invoke(
    input = 'Quem foi Nietzche',
    temperature = 1,
    max_tokens = 500
    )

print(response)