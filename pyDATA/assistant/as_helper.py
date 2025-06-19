import openai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
print("✅ API Key Found:", openai.api_key)

# Create Assistant
assistant = openai.beta.assistants.create(
    name="Resume Assistant",
    instructions="You help users write professional resumes. Ask their name, education, skills, and experience.",
    model="gpt-4"
)

print("✅ Assistant Created")
print("Assistant ID:", assistant.id)