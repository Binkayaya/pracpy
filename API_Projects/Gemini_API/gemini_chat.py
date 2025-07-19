import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# Set your API key here
API_KEY = os.getenv("API_KEY")

genai.configure(api_key=API_KEY)

# Load the Gemini Pro model
model = genai.GenerativeModel("models/gemini-1.5-flash")

# Start a chat session
chat = model.start_chat(history=[])

print("?? Gemini Chatbot (type 'exit' to quit)")
while True:
    msg = input("You: ")
    if msg.lower() == "exit":
        break
    response = chat.send_message(msg)
    print("Gemini:", response.text)





    