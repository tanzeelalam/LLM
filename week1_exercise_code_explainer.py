# imports
import os
from dotenv import load_dotenv
from openai import OpenAI
from IPython.display import Markdown, display, update_display

# constants
MODEL_GPT = 'gpt-4o-mini'
MODEL_LLAMA = 'llama3.2'

# set up environment
load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

# Check the key

if api_key:
    print("API key found and looks good so far!")
else:
    print("API key not found")

code_snippet = 'yield from {book.get("author") for book in books if book.get("author")}'

system_prompt = "You are a code expert, you need to explain in detail the provided code snippet"
user_prompt = "Can you explain the following piece of code."
user_prompt += code_snippet

messages =  [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]

def AnanlyzeAndAnswer(selected_model: str):
    if selected_model == MODEL_GPT:
        openai = OpenAI()
        response = openai.chat.completions.create(
            model= MODEL_GPT,
            messages= messages,
            stream=True
        )
        print(f"MODEL : {MODEL_GPT}")
    else:
        ollama_via_openai = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')
        response = ollama_via_openai.chat.completions.create(model=MODEL_LLAMA, messages=messages)
        print(f"MODEL : {MODEL_LLAMA}")

    return response.choices[0].message.content

#print(AnanlyzeAndAnswer(MODEL_GPT))
print(AnanlyzeAndAnswer(MODEL_LLAMA))