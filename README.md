# Ai-Chatbot
An AI Chatbot web application built using Django, integrating NLP for text-based and voice-based user interaction, powered by a knowledge base about Artificial Intelligence. Supports text and voice input, responds with related knowledge from the knowledge base, and provides a clean interface with speech synthesis.                          

# AI Chatbot - Django Web Application

An AI-powered Chatbot built with **Django**, designed to answer questions related to Artificial Intelligence. The chatbot supports both **text input** and **voice input**, provides responses by searching a predefined knowledge base, and speaks answers using **text-to-speech (TTS)**.

---

## 🚀 Features

- Text-based user query input
- Voice-based user input with Speech Recognition
- Text-to-Speech functionality for bot responses
- Intelligent knowledge base lookup
- Answers include main sentence + additional context when applicable
- Simple and clean front-end with background image and styled conversation
- Conversation history shown on the webpage

---

## ⚙️ Technologies Used

- Python 3.x
- Django Web Framework
- NLTK (Natural Language Toolkit)
- scikit-learn (TF-IDF Vectorizer & Cosine Similarity)
- pyttsx3 (Text-to-Speech)
- SpeechRecognition
- HTML + CSS (inline styling)

---

## 📁 Project Structure

- `ai_knowledge.txt` → Contains knowledge base sentences about Artificial Intelligence
- `views.py` → Main logic for processing user queries and generating responses
- `chatbot.html` → Frontend template displaying the chatbot interface
- Static assets folder for images (background, etc.)

---

## ⚡ Installation & Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/ai-chatbot.git
    ```

2. Ensure the `ai_knowledge.txt` file is placed in the correct location.

3. Run migrations:
    ```bash
    python manage.py migrate
    ```

4. Run the Django server:
    ```bash
    python manage.py runserver
    ```

5. Open your browser and visit:
    ```
    http://127.0.0.1:8000/
    ```

---

## ✅ Usage

- Type a question related to Artificial Intelligence in the input field and click **Ask**
- Or click **Speak** and use your microphone to ask a question aloud
- The chatbot provides an answer along with additional context if available
- The conversation history is displayed in the browser
- Bot responses are also spoken aloud when using voice input

---

## ⚠️ Notes

- The chatbot is specialized in answering only AI-related queries
- If the query is vague or unrelated, it prompts the user to ask AI-specific questions
- Speech recognition requires a working microphone
- Text-to-Speech is handled in a thread to prevent blocking the main server

---

##  Acknowledgements

Inspired by the advancements in AI, NLP, and conversational agents.

