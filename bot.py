import os
import random
import re
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
greetings = ["hello", "hi", "hey", "greetings", "good morning", "good afternoon", "good evening"]
how_are_you_questions = ["how are you", "how's it going", "how do you do", "what's up", "how have you been", "how's everything", "how's life", "wassup"]
farewell = ["bye", "goodbye", "see you later", "take care", "farewell"]
thanks = ["thanks", "thank you", "much appreciated", "thanks a lot", "thank you very much"]
greeting_responses = ["Hello!", "Hi there!", "Hey!", "Greetings!"]

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

while True:
    user_input = input("Enter something: ").strip()
    if user_input.lower() in farewell:
        print("Chatbot:", random.choice(farewell))
        break
    elif re.search(r"\bhello\b", user_input.lower()):
        print("Chatbot:", random.choice(greeting_responses))
    elif user_input.lower() in thanks:
        print("Chatbot: You're welcome!")
    elif user_input.lower() == "help":
        print("Chatbot: You can greet me, ask how I am, say thanks, or say goodbye.")
    elif user_input.lower() in how_are_you_questions:
        print("Chatbot: I'm just a program, but I'm doing well!")
    else:
        response = model.generate_content(user_input)
        print("Chatbot:", response.text)
