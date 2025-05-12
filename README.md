🚨 Cyberbullying Detection Web App 🧠💬
A fully responsive, animated, and interactive web application that uses Natural Language Processing (NLP) and Machine Learning to detect cyberbullying in real-time user input. This project is aimed at promoting safe digital communication by classifying harmful or toxic messages using intelligent text analysis.

🧪 Demo
🎥 A glimpse of the app in action:

✅ Real-time predictions

✅ Animated processing steps: Processing..., Analyzing..., Predicting...

✅ Results shown and then auto-hidden after 5 seconds

✅ Elegant UI with cyberbullying awareness visuals

✅ Seamless keyboard support (Enter to submit)

🧰 Tech Stack
🧠 Machine Learning & NLP:
TF-IDF Vectorizer: Converts raw text into numerical features

Logistic Regression: Binary text classification model

NLP Techniques:

Text cleaning (lowercasing, punctuation removal)

Tokenization

Stopword removal

Vectorization

🌐 Web Development:
Frontend:

HTML5, CSS3

Bootstrap 5

JavaScript (ES6)

Animate.css for transitions and effects

Backend:

Python with Flask

Pickled .pkl files for ML model and vectorizer

Design:

Custom hero images from static assets

Dark-themed navbar and vibrant gradients inspired by the primary hero image

Responsive layout and animated elements

🚀 Features
🌐 Multi-page structure: Home, About, Help, Contact

🔥 Real-time feedback with a 3-step animation for prediction process

⌨️ Keyboard accessibility with Enter key submission

📉 Auto-hide prediction results after 5 seconds

🧩 Word count analytics and confidence scoring

📷 Cyberbullying awareness images and themed design

📲 Fully responsive UI for mobile and desktop

🧠 Dataset & Model
The model was trained on a cleaned cyberbullying dataset (source: Kaggle), labeled into binary categories (cyberbullying vs. non-cyberbullying). The .pkl files used in deployment include:

tfidf_vectorizer.pkl

cyberbully_model.pkl

For privacy reasons, dataset is not included. You may use any relevant text classification dataset for retraining.

📌 To-Do / Enhancements
 Add multilingual support for non-English inputs

 Improve classification granularity (hate speech, insult, threat, etc.)

 Host publicly via Docker/Heroku/Render

 Add chatbot integration for continuous feedback

 Store analysis logs in database (MongoDB/PostgreSQL)

🤝 Contributing
Want to contribute? Fork the repo, create a feature branch, and submit a PR. Feel free to open issues or share suggestions.

📃 License
This project is licensed under the MIT License.

🔗 Let's Connect
🌐 LinkedIn Profile

📂 Project Showcase

💬 For collaboration: open an issue or contact me directly

💬 Final Note
This project aims to use AI for social good. It is not perfect but a step toward building safer digital spaces using the power of NLP and Machine Learning. Always open to feedback, collaboration, or improvement ideas!
