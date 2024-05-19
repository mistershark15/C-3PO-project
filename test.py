import pygame
import time
import os
import json
import speech_recognition as sr
from googlesearch import search
import requests

# Inicializace přehrávače zvuku
pygame.init()

# Nastavení cesty k adresáři se zvuky
SOUND_DIR = "sounds"

# Cesta k souboru s uloženými informacemi
INFO_FILE = "info.json"

# Funkce pro přehrávání zvuku
def play_sound(filename):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# Funkce pro vyhledání odpovědi online
def search_online(query):
    try:
        search_results = search(query, num_results=1)
        response = requests.get(search_results[0])
        return response.text
    except Exception as e:
        return f"An error occurred while searching online: {str(e)}"

# Funkce pro načtení uložených informací
def load_info():
    if os.path.exists(INFO_FILE):
        with open(INFO_FILE, 'r') as file:
            return json.load(file)
    return {}

# Funkce pro uložení informací
def save_info(info):
    with open(INFO_FILE, 'w') as file:
        json.dump(info, file)

# Funkce pro normalizaci dotazů
def normalize_query(query):
    return query.lower().strip()

# Funkce pro získání odpovědi od uživatele pomocí mikrofonu
def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
    try:
        response = recognizer.recognize_google(audio)
        print(f"You: {response}")
        return response
    except sr.UnknownValueError:
        print("C-3PO: Sorry, I did not understand that.")
        return None
    except sr.RequestError as e:
        print(f"C-3PO: Could not request results; {e}")
        return None

# Funkce pro odpověď na dotaz
def respond(query, info):
    normalized_query = normalize_query(query)
    if normalized_query in ["hello", "hi", "good morning"]:
        print("C-3PO: Hello! How can I assist you today?")
        play_sound(os.path.join(SOUND_DIR, "hello.mp3"))
    elif normalized_query in ["bye", "goodbye"]:
        print("C-3PO: Goodbye!")
        play_sound(os.path.join(SOUND_DIR, "bye.mp3"))
    elif normalized_query in ["what is your name", "whats your name", "who are you"]:
        print("C-3PO: I'm C-3PO, human-cyborg relations.")
        play_sound(os.path.join(SOUND_DIR, "name.mp3"))
    elif normalized_query.startswith("do you know"):
        topic = normalize_query(normalized_query[11:].strip())
        if topic in info:
            print(f"C-3PO: Yes, I know about {topic}. {info[topic]}")
            play_sound(os.path.join(SOUND_DIR, "yes_know.mp3"))
        else:
            print(f"C-3PO: No, I don't know about {topic}. Can you tell me about it?")
            play_sound(os.path.join(SOUND_DIR, "no_dont_know.mp3"))
            new_info = get_voice_input()
            if new_info:
                info[topic] = new_info
                save_info(info)
                print(f"C-3PO: Thank you! I've learned about {topic}.")
                play_sound(os.path.join(SOUND_DIR, "thank_you.mp3"))
    elif normalized_query.startswith("who is") or normalized_query.startswith("what is"):
        topic = normalize_query(normalized_query[6:].strip())
        if topic in info:
            print(f"C-3PO: {info[topic]}")
        else:
            response = search_online(query)
            print("C-3PO: " + response)
    else:
        response = search_online(query)
        print("C-3PO: " + response)

# Hlavní smyčka pro interakci s uživatelem
def main():
    ascii_art = """
    \033[93m
    *********************************************
    *  ______        ____   .______     ______  *
    * /      |      |___ \  |   _  \   /  __  \ *
    *|  ,----' ______ __) | |  |_)  | |  |  |  |*
    *|  |     |______|__ <  |   ___/  |  |  |  |*
    *|  `----.       ___) | |  |      |  `--'  |*
    * \______|      |____/  | _|       \______/ *
    *********************************************
    \033[0m
    """
    print(ascii_art)
    print("Welcome! Speak or type a query and C-3PO will try to respond (type 'exit' to quit).")
    recognizer = sr.Recognizer()
    info = load_info()
    while True:
        print("Listening...")
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio)
            print(f"You: {query}")
            if query.lower() == "exit":
                break
            respond(query, info)
        except sr.UnknownValueError:
            print("C-3PO: Sorry, I did not understand that.")
        except sr.RequestError as e:
            print(f"C-3PO: Could not request results; {e}")

# Spuštění hlavní funkce
if __name__ == "__main__":
    main()
