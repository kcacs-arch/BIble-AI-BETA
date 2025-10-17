import os
import gradio as gr
from google import genai

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

chat_session = None

def get_response(message, history):
    global chat_session
    
    if len(history) == 0:
        chat_session = client.chats.create(
            model=MODEL_NAME,
            config=genai.types.GenerateContentConfig(system_instruction=SYSTEM_INSTRUCTION)
        )
    
    user_message = message if isinstance(message, str) else message["content"]
    reply = chat_session.send_message(user_message)
    return reply.text

demo = gr.ChatInterface(
    fn=get_response,
    title="Biblical AI Counselor",
    description="Rooted in the Holy Bible — not modern philosophy.",
    textbox=gr.Textbox(placeholder="Ask about life, Scripture, or wisdom.", container=False, scale=7),
    chatbot=gr.Chatbot(height=500, type="messages"),
    type="messages"
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=5000)

