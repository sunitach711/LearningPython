import openai
import os
from import load_dotenv

load_dotenv()

# नया API तरीका: OpenAI क्लाइंट ऑब्जेक्ट बनाएं
# सुनिश्चित करें कि OPEN_AI_KEY पर्यावरण वेरिएबल में सेट है।
client = openai.OpenAI(api_key=os.getenv('OPEN_AI_KEY'))



response = client.chat.completions.create(
    model='gpt-3.5-turbo', # 'gpt-4-turbo' की जगह 'gpt-3.5-turbo' का उपयोग करें
    messages=[
        {
            'role': 'user',
            'content': 'what is chatgpt agent?'
        }
    ],
    temperature=1,
    max_tokens=256,
)

# API response को सही ढंग से एक्सेस करने के लिए
print(response.choices[0].message.content)