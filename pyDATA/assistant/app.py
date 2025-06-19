from flask import Flask, render_template, request, jsonify
import openai
import os
from dotenv import load_dotenv
import time

app = Flask(__name__)

# Load API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
assistant_id = "asst_QPHKXNDMglxzC06WfkG7or0S"

# Store thread per session (for demo, use a global thread)
thread = openai.beta.threads.create()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "No message provided."}), 400

    # Send user message
    openai.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=user_message
    )

    # Run assistant
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

    # Get assistant response
    messages = openai.beta.threads.messages.list(thread_id=thread.id)
    for msg in messages.data:
        if msg.role == "assistant":
            return jsonify({"response": msg.content[0].text.value})
    return jsonify({"response": "Sorry, no response from assistant."})

@app.route("/chatgpt")
def chatgpt():
    return render_template("chatgpt.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
