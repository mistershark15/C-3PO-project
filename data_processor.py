# data_processor.py

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter
import os

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def preprocess_data(data):
    processed_text = []
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    for sentence in data:
        words = word_tokenize(sentence.lower())
        processed_words = [lemmatizer.lemmatize(word) for word in words if word.isalnum() and word not in stop_words]
        processed_text.extend(processed_words)
    return processed_text

def train_model(data_dir):
    # Implementace trénování modelu z dat uložených v dané složce
    pass
