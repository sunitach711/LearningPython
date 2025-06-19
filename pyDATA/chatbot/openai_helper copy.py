from openai import OpenAI

client = OpenAI(api_key=os.getenv('OPEN_AI_KEY'))
import os
from dotenv import load_dotenv

load_dotenv()


response = client.chat.completions.create(model='gpt-4.1',
message=[
     {  
         'role': 'user',
         'content': 'color of sky'
     }
],
temperature=1,
max_tokens=256)


print(response)

