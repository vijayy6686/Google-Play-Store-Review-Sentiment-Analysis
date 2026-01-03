# 📱 Google Play Store Review Sentiment Analysis

🌟 Multiclass Sentiment Analysis Web Application

📖 Project Overview

The Google Play Store Review Sentiment Analysis project is an end-to-end machine learning web application that classifies user reviews into Positive, Negative, or Neutral sentiments using Natural Language Processing (NLP) techniques.

This project demonstrates the complete lifecycle of a text-based machine learning system, including data preprocessing, feature extraction, model training, evaluation, and deployment through an interactive web interface.

Users can input real Google Play Store–style reviews and receive instant sentiment predictions. The application emphasizes clean ML engineering practices, transparent modeling, and realistic evaluation, avoiding exaggerated performance claims.

📊 Dataset Information

Real-world Google Play Store user reviews

Labeled with three sentiment classes

Reflects authentic user feedback containing:

Informal language

Typos and abbreviations

Short, unstructured sentences

Includes neutral opinions alongside positive and negative feedback

Problem Type: Supervised Multiclass Text Classification

🔹 Key Dataset Characteristics

Raw user review text

Noisy, real-world linguistic patterns

Multiclass sentiment labels

Suitable for NLP-based sentiment analysis

🎯 Target Variable

Sentiment Label

Label	Meaning
Positive	Favorable user sentiment
Neutral	Mixed or informational sentiment
Negative	Unfavorable user sentiment

Objective:
Accurately classify unseen reviews into one of the three sentiment categories based on learned textual patterns.

🧠 Methodology

The project follows a supervised multiclass machine learning approach using NLP techniques.

🔸 Text Preprocessing

Lowercasing text

Removal of punctuation and special characters

Stopword removal

Whitespace normalization

Identical preprocessing during training and inference

🔸 Feature Extraction

TF-IDF (Term Frequency–Inverse Document Frequency)

Converts raw text into numerical feature vectors

Captures word importance across the entire corpus

🔸 Model Training

Logistic Regression (Multiclass Classification) using scikit-learn

Trained on TF-IDF features

Uses a one-vs-rest (OvR) or multinomial strategy (solver-dependent)

Evaluated using:

Accuracy

Precision

Recall

F1-score (macro and weighted)

🔸 Model Persistence

TF-IDF vectorizer and Logistic Regression model saved together as a single pipeline using joblib

Ensures:

Consistent preprocessing during inference

No retraining at runtime

Reproducibility and maintainability

🖥️ Web Application Implementation

The application is implemented using Streamlit, providing a clean and interactive user interface.

🔹 Implementation Highlights

Text input for user reviews

Real-time sentiment prediction on button click

Probability-based output for each sentiment class

Minimal dark-themed UI using embedded HTML & CSS

Direct inference using the trained ML pipeline

Backend strictly performs sentiment classification without fabricated emotional scores or explanations

📂 Repository Structure
google-play-store-review-sentiment-analysis/
│
├── app.py
│   ├── Streamlit web application
│   ├── Handles user input
│   ├── Loads trained ML pipeline
│   └── Performs real-time multiclass sentiment prediction
│
├── reviews_pipeline.pkl
│   └── Serialized TF-IDF + Logistic Regression pipeline
│
├── requirements.txt
│   └── Python dependencies
│
├── README.md
│   └── Project documentation
│
└── .gitignore
    └── Excludes virtual environments and cache files

🛠️ Tech Stack
🔹 Programming Language

Python 3.9+

🔹 Machine Learning & NLP

scikit-learn

TF-IDF

Logistic Regression (Multiclass)

Pipelines

joblib – model serialization

🔹 Data Processing

pandas

🔹 Web Application

Streamlit

🔹 Frontend Styling

Embedded HTML & CSS (custom dark UI)

🔹 Deployment (Optional)

Streamlit Community Cloud

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py

✅ Conclusion

This project demonstrates a real-world multiclass NLP sentiment analysis workflow, emphasizing:

Consistent and correct text preprocessing

TF-IDF–based feature engineering

Multiclass Logistic Regression modeling

Responsible evaluation practices

Clean and reliable Streamlit deployment
