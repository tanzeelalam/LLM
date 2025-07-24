# imports
from openai import OpenAI

# Create a messages list using the same format that we used for OpenAI

messages = [
    {"role": "user", "content": "Describe some of the business applications of Generative AI"}
]

ollama_via_openai = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')

response = ollama_via_openai.chat.completions.create(model="llama3.2", messages=messages)
print(response.choices[0].message.content)