import nltk

nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("punkt_tab")

from flask import Flask, request, render_template
import joblib
import re, string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Load model and vectorizer
model = joblib.load("cyberbully_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")


# Initialize Flask
app = Flask(__name__)


# Preprocessing function
def preprocess(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)
    text = re.sub(r"@\w+|#", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    tokens = word_tokenize(text)
    tokens = [w for w in tokens if w not in stopwords.words("english")]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return " ".join(tokens)


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        input_text = request.form["text"]
        clean_text = preprocess(input_text)
        vec = vectorizer.transform([clean_text])
        prediction = model.predict(vec)[0]
        return render_template("index.html", prediction=prediction, text=input_text)
    proba = model.predict_proba(vec)[0]
    confidence = round(max(proba) * 100, 2)

    return render_template(
        "index.html", prediction=prediction, text=input_text, confidence=confidence
    )


if __name__ == "__main__":
    app.run(debug=True)
