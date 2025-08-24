from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

template = '''
Traduza o texto de {idioma1} para {idioma2}: {texto}
'''

prompt_template = PromptTemplate.from_template(template=template)

prompt = prompt_template.format(
    idioma1 = 'inglês', 
    idioma2 = 'português',
    texto = 'How old are you?'
)

model = ChatOpenAI(
    model = 'gpt-3.5-turbo'
)

response = model.invoke(prompt)

print(response.content)

