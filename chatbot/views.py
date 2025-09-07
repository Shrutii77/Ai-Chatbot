from django.shortcuts import render
from django.http import JsonResponse
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pyttsx3
import speech_recognition as sr
import re
import threading
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')

recognizer = sr.Recognizer()
lemmatizer = WordNetLemmatizer()

with open('ai_knowledge.txt', 'r', encoding='utf-8') as f:
    knowledge_base = f.read()

sentences = sent_tokenize(knowledge_base)
vectorizer = TfidfVectorizer()
vectorized_sentences = vectorizer.fit_transform(sentences)

conversation_history = []

def speak(text):
    def run():
        engine = pyttsx3.init()  # Initialize engine inside thread
        engine.say(text)
        engine.runAndWait()
    threading.Thread(target=run).start()

def normalize_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    text = text.replace("artificial intelligence", "ai")
    terms = re.findall(r'\b\w+\b', text)
    lemmatized_terms = [lemmatizer.lemmatize(term) for term in terms]
    return ' '.join(lemmatized_terms).strip()

def get_response_text(query):
    normalized_query = normalize_text(query)
    if normalized_query in ['ai', 'what is ai', 'define ai', 'introduction to ai']:
        for sentence in sentences:
            normalized_sentence = normalize_text(sentence)
            if 'ai refers to' in normalized_sentence or 'ai is' in normalized_sentence:
                return sentence  # Return the first good introductory sentence found
    query_terms = re.findall(r'\b\w+\b', normalized_query)

    if len(query_terms) < 2 or normalized_query == 'future':
        return "Hmm… that’s interesting! But I’m only trained to talk about Artificial Intelligence. Try asking me about AI"

    key_terms = ['ai', 'artificial', 'intelligence', 'machine', 'learning', 'nlp', 'natural', 'processing']
    if not any(term in normalized_query for term in key_terms):
        return "Hmm… that’s interesting! But I’m only trained to talk about Artificial Intelligence. Try asking me about AI"

    for i, sentence in enumerate(sentences):
        normalized_sentence = normalize_text(sentence)
        if normalized_query in normalized_sentence:
            main_response = sentence

            additional_sentences = []
            next_index = i + 1
            while next_index < len(sentences) and len(additional_sentences) < 2:
                next_sentence = sentences[next_index].strip()
                
                # Stop if new topic or section starts (line ending with ':')
                if next_sentence.endswith(':') or len(next_sentence.split()) < 8:
                    break

                additional_sentences.append(next_sentence)
                next_index += 1

            full_response = main_response
            if additional_sentences:
                full_response += "\n\nAdditional Info:\n" + "\n".join(additional_sentences)
            return full_response

    return "Hmm… that’s interesting! But I’m only trained to talk about Artificial Intelligence. Try asking me about AI"

def chatbot(request):
    user_query = ''
    response = ''

    if request.method == 'POST':
        action = request.POST.get('action')  # "speak" for microphone input
        user_query = request.POST.get('query', '').strip()

        if action == 'speak' and not user_query:
            try:
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source)
                    print("Listening… Please speak now.")
                    audio = recognizer.listen(source)
                    user_query = recognizer.recognize_google(audio)
            except sr.UnknownValueError:
                response = "Sorry, I didn't catch that."
                conversation_history.append(('You', ' (voice input)'))
                conversation_history.append(('Bot', response))
                speak(response)
                return render(request, 'chatbot.html', {'response': response, 'conversation': conversation_history})
            except Exception as e:
                response = "Voice recognition failed."
                conversation_history.append(('You', '(voice input)'))
                conversation_history.append(('Bot', response))
                speak(response)
                return render(request, 'chatbot.html', {'response': response, 'conversation': conversation_history})

        if user_query.lower() == "can we speak out loud":
            response = "Sorry, I can't speak to you in voice yet. This feature will be available soon."
        elif user_query:
            response = get_response_text(user_query)
        else:
            response = "Please type a query or use the microphone."

        conversation_history.append(('You 🤵‍♂️', user_query))
        conversation_history.append(('Bot 🤖', response))

        if action == 'speak':
            speak(response)


    return render(request, 'chatbot.html', {'response': response, 'conversation': conversation_history})

