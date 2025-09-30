from flask import Flask, request, render_template_string
import os
import random
import re
from dotenv import load_dotenv
import google.generativeai as genai
from chatbotlists import greetings, farewell, thanks, greeting_responses, how_are_you_questions

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")
app = Flask(__name__)

HTML="""
<!doctype html>
<title>AI Chatbot</title>
<style>
body {
    font-family: Arial, sans-serif;
    background: #f4f4f4;
    margin: 0;
    padding: 0;
    }
<h1>Chat with the AI</h1>
<form method=post>
  <input name=user_input autofocus>"
  <input type=submit value=Send>
</form>
{% if response %}
  <p><b>Chatbot:</b> {{ response }}</p>
{% endif %}
"""

def get_chatbot_response(user_input):
    if user_input.lower() in farewell:
        return random.choice(farewell)
    elif re.search(r"\bhello\b", user_input.lower()):
        return random.choice(greeting_responses)
    elif user_input.lower() in thanks:
        return "You're welcome!"
    elif user_input.lower() == "help":
        return "You can greet me, ask how I am, say thanks, or say goodbye."
    elif user_input.lower() in how_are_you_questions:
        return "I'm just a program, but I'm doing well!"
    else:
        response = model.generate_content(user_input)
        return response.text

@app.route("/", methods=["GET", "POST"])
def chat():
    response = None
    if request.method == "POST":
        user_input = request.form["user_input"]
        response = get_chatbot_response(user_input)
    return render_template_string(HTML, response=response)
    

if __name__ == "__main__":
    app.run(debug=True)