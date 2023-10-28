from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pickle


def preprocess_text(text):
    words = word_tokenize(text)
    words = [
        word.lower()
        for word in words
        if word.isalnum() and word.lower() not in stopwords.words("english")
    ]
    return words


def extract_features(text):
    return {word: True for word in text}


with open("mynltk/classifier.pkl", "rb") as f:
    classifier = pickle.load(f)


def classify_text(text):
    features = extract_features(preprocess_text(text))
    return classifier.classify(features)


def do_classify(text: str) -> dict[str, int]:
    result = classify_text(text)
    m = {
        0: "extraversion",
        1: "neuroticism",
        2: "agreeableness",
        3: "conscientiousness",
        4: "openness",
    }
    res = {}
    for i, x in enumerate(result):
        res[m[i]] = x
        print(f"{m[i]}: {x}")
    return res
