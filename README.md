# Basic-AI-Chatbot

A beginner-friendly AI chatbot designed for easy setup and development. It comes with built-in responses for general conversation and leverages the Gemini API to handle queries beyond its predefined scope

## 🚀 Features
- Simple and intuitive architecture for quick deployment
- Predefined responses for common interactions
- Gemini API integration for dynamic, intelligent replies
- Easy to extend and customize

## 🔧 Setup Instructions
- Clone the repository.
- Create a .env file in the root directory.
- Add your Gemini API key to the .env file:
```GEMINI_API_KEY=your_api_key_here```
- ⚠️ Important: Do not hardcode your API key directly into the source code. Use environment variables for security.
- Run bot.py to start the chatbot.


## 🌐 Web Chatbot (Flask)

You can now run the chatbot as a web app using Flask:

### How to Run the Web Chatbot

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   pip install flask
   ```
Ignore this step if you have already installed requirements.txt


2. **Set your Gemini API key:**
   - Create a `.env` file in the project root.
   - Add your API key:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```
Ignore this step if you had already created a .env file and set the API key

3. **Start the web server:**
   ```bash
   python app.py
   ```
   - If port 5000 is busy, change the port in `app.py`:
     ```python
     app.run(debug=True, port=5001)
     ```

4. **Open your browser:**
   - Go to `http://localhost:5000` (or the port you chose).

### Features
- Simple web interface for chatting with the AI.
- Handles greetings, farewells, thanks, and “how are you” questions.
- Uses Gemini AI for other responses.

## 🤝 Contributing
We welcome contributions from developers of all skill levels! Here's how you can get involved:
- Fork the repository.
- Clone your fork to your local machine.
- Create a new branch for your feature or fix:
 ```git checkout -b feature-name```
- Make your changes and commit them:
```git commit -m "Add feature or fix"```
- Push to your fork:
```git push origin feature-name```
- Open a pull request on the original repository.
Please follow best practices for code quality and include clear commit messages. If you're adding a new feature, consider updating the README as well.

## 📄 License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.


