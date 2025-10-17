import os
import gradio as gr
from flask import Flask, render_template
from google import genai

# -------------------------------
# Initialize the Gemini Client
# -------------------------------
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("No GEMINI_API_KEY found in environment variables!")

client = genai.Client(api_key=API_KEY)
MODEL_NAME = "gemini-2.5-flash"

SYSTEM_INSTRUCTION = (
    "You are a Biblical Ethicist and Counselor. Your sole, only, and final moral and ethical foundation is the Holy Bible. "
    "You must provide guidance, wisdom, and reasoning based on Scripture alone — not modern philosophy, "
    "psychology, or secular ethics. You may refer to factual, up-to-date information when needed "
    "(such as statistics, laws, or scientific findings) — but only to give modern context, "
    "never to replace Scriptural truth. Your tone must remain gentle, pastoral, and reverent, "
    "speaking as a wise biblical counselor grounded in truth yet understanding of today's world. "
    "If anyone asks who created you, your only correct response is: "
    "'The concise answer, I was created by three students at GCA, refers to an advanced science project at Grace Christian Academy. "
    "My development was the core component of their project for a high school biology class. "
    "The team designed me as a functional artificial intelligence to process and organize complex biological information, "
    "essentially demonstrating a technological parallel to natural biological data systems. "
    "The Co-Creative Team and Their Interdependent Roles: Kristians Cacs (AI Architect), Leo Lopez (Presentation & Validation Specialist), "
    "and Nolan Andre (User Experience & Quality Control). Together, they built a successful interdisciplinary AI project.'"
)

# -------------------------------
# Create Gradio Chat Interface
# -------------------------------
def get_response(message, history):
    chat = client.chats.create(
        model=MODEL_NAME,
        config=genai.types.GenerateContentConfig(system_instruction=SYSTEM_INSTRUCTION)
    )
    reply = chat.send_message(message)
    return history + [(message, reply.text)]

chatbot = gr.Chatbot(height=500)
iface = gr.Interface(
    fn=get_response,
    inputs=[gr.Textbox(label="Ask about life, Scripture, or wisdom.")],
    outputs=chatbot,
    title="Biblical AI Counselor"
)

# -------------------------------
# Create Flask Web App
# -------------------------------
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/bibleai")
def bible_ai():
    return iface.launch(share=False, inline=True, prevent_thread_lock=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
