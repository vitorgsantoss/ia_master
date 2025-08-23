from langchain_community.cache import SQLiteCache
from langchain.globals import set_llm_cache
from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

model = OpenAI()

set_llm_cache(
    SQLiteCache(database_path='cache_langchain.db')
)

prompt = 'Quem foi Napoleão'

response1 = model.invoke(prompt)
print('Response 1: ', response1)

response2 = model.invoke(prompt)
print('Response 1: ', response2)