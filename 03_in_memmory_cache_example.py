from langchain_openai import OpenAI
from langchain_community.cache import InMemoryCache
from langchain.globals import set_llm_cache
from dotenv import load_dotenv

load_dotenv()

model = OpenAI()

# set_llm_cache(InMemoryCache())

response1 = model.invoke('Me diga que foi Guido VonRossum')
print(response1)

response2 = model.invoke('Me diga que foi Guido VonRossum')
print(response2)