import openai
import os
from dotenv import load_dotenv
import time

# Step 1: Load API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
assistant_id = "asst_QPHKXNDMglxzC06WfkG7or0S"

# Step 2: Create threads
thread = openai.beta.threads.create()

# Step 3: Intial message
openai.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="I need a professional resume for a software engineer position."
)

# Step 4: Run Assistant (First response)
run = openai.beta.threads.runs.create(
    assistant_id=assistant_id,
    thread_id=thread.id
)


# Wait for completion
while True:
    run_status = openai.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
    if run_status.status == "completed":
        break
    time.sleep(1)

# Show first asssistant response
messages = openai.beta.threads.messages.list(thread_id=thread.id)
for msg in reversed(messages.data):
    if msg.role == "assistant":
        print("Assistant:", msg.content[0].text.value)

time.sleep(5)  # Wait before next step

        
# Step 5: User provides details
openai.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="""
    My name is Sunita Chahar.
    I graduated with a B.Tech in Computer Science from XYZ University in 2021.
    I have 3 years of experience as a Python Developer at ABC Tech Pvt. Ltd.
    I worked on backend systems using Python and Django, building RESTful APIs and managing PostgreSQL databases.
    My technical skills include Python, Django, REST APIs, SQL, and Git.
    I am certified in Backend Development by Coursera.
    I have also led a project to automate internal reporting systems, reducing manual workload by 40%.
    """
)

# Step 6: Run Assistant again with your info
run2 = openai.beta.threads.runs.create(
    assistant_id=assistant_id,
    thread_id=thread.id
)

# Wait for second response
while True:
    run_status2 = openai.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run2.id)
    if run_status2.status == "completed":
        break
    time.sleep(1)

# Step 7: Show final resume response
messages2 = openai.beta.threads.messages.list(thread_id=thread.id)
for msgs in messages2.data:
    if msgs.role == "assistant":
        print("\n🧾 Final Resume Output:\n")
        print(msgs.content[0].text.value)
        break