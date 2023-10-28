import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import apply_features

import pickle
import csv


data = pd.read_csv("essays.csv", encoding="latin-1", sep=",")

nltk.download("stopwords")
nltk.download("punkt")


def preprocess_text(text):
    words = word_tokenize(text)
    words = [
        word.lower()
        for word in words
        if word.isalnum() and word.lower() not in stopwords.words("english")
    ]
    return words


data["TEXT"] = data["TEXT"].apply(preprocess_text)
data["cEXT"] = (data["cEXT"] == "y").astype(int)
data["cNEU"] = (data["cNEU"] == "y").astype(int)
data["cAGR"] = (data["cAGR"] == "y").astype(int)
data["cCON"] = (data["cCON"] == "y").astype(int)
data["cOPN"] = (data["cOPN"] == "y").astype(int)


def extract_features(text):
    return {word: True for word in text}


train_features = [
    (extract_features(text), (attrs[0], attrs[1], attrs[2], attrs[3], attrs[4]))
    for (text, attrs) in zip(
        data["TEXT"], data[["cEXT", "cNEU", "cAGR", "cCON", "cOPN"]].values
    )
]

classifier = NaiveBayesClassifier.train(train_features)

data["cEXT"] = data["cEXT"].astype(str)
data["cNEU"] = data["cNEU"].astype(str)
data["cAGR"] = data["cAGR"].astype(str)
data["cCON"] = data["cCON"].astype(str)
data["cOPN"] = data["cOPN"].astype(str)


with open("classifier.pkl", "wb") as f:
    pickle.dump(classifier, f)
