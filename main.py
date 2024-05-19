# main.py

import nltk
from web_scraper import scrape_website
from data_processor import preprocess_data, train_model
import os
import random

# Nastavení cesty pro ukládání dat
DATA_DIR = "data"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Webové stránky, ze kterých se C-3PO bude učit
WEBSITE_URLS = [
    "https://en.wikipedia.org/wiki/Artificial_intelligence",
    "https://en.wikipedia.org/wiki/Machine_learning",
    "https://openlibrary.org/collections/star-wars",
    "http://www.randompassages.com/",
    "https://en.wikipedia.org/wiki/Animal",
    "https://en.wikipedia.org/wiki/World",
    "https://en.wikipedia.org/wiki/Fish",
    "https://www.youtube.com/",
    "https://www.instagram.com/",
    "https://en.wikipedia.org/wiki/English_language",
    "https://www.umimeanglicky.cz/grammar",

    # Další webové stránky...
]

# Vybrání náhodné webové stránky pro učení
selected_urls = random.sample(WEBSITE_URLS, k=3)

# Načtení dat ze zvolených webových stránek
for url in selected_urls:
    raw_data = scrape_website(url)
    preprocessed_data = preprocess_data(raw_data)
    
    # Uložení předzpracovaných dat
    filename = os.path.join(DATA_DIR, f"{url.split('/')[-1]}.txt")
    with open(filename, "w", encoding="utf-8") as file:
        for sentence in preprocessed_data:
            file.write(sentence + "\n")

# Trénování modelu na načtených datech
train_model(DATA_DIR)
