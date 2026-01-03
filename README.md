# 📱 Google Play Store Review Sentiment Analysis

🌟 Sentiment Analysis Web Application

📖 Project Overview

The Google Play Store Review Sentiment Analysis project is an end-to-end machine learning web application that classifies user reviews into Positive, Neutral, or Negative sentiments using Natural Language Processing (NLP).

The project demonstrates the complete lifecycle of a text-based ML system — from preprocessing and feature extraction to model training and deployment via an interactive web interface.

Users can input real Google Play Store–style reviews and receive instant sentiment predictions. The focus is on clean ML engineering practices, transparent modeling, and realistic evaluation, not exaggerated metrics.

📊 Dataset Information

The dataset consists of real-world Google Play Store user reviews labeled by sentiment.
It reflects authentic user feedback with diverse writing styles, vocabulary, and emotional expressions.

The dataset is suitable for a supervised multiclass text classification problem.

🔹 Key Features

Raw user review text

Informal language, typos, and short sentences

Presence of positive, neutral, and negative sentiments

🎯 Target Variable

Sentiment Label

Positive

Neutral

Negative

Objective:
Accurately classify unseen reviews based on learned textual patterns.

🧠 Methodology

The project follows a supervised machine learning approach using NLP techniques.

🔸 Text Preprocessing

Lowercasing text

Removal of punctuation and special characters

Stopword removal

Whitespace normalization

Consistent preprocessing during both training and inference

🔸 Feature Extraction

TF-IDF (Term Frequency–Inverse Document Frequency)

Converts text into numerical vectors

Preserves important word-importance patterns

🔸 Model Training

Logistic Regression (Multiclass Classification) using scikit-learn

Trained on TF-IDF features

Evaluated using accuracy, precision, recall, and F1-score

🔸 Model Persistence

TF-IDF vectorizer and Logistic Regression model saved together using joblib

Ensures consistent preprocessing and predictions during deployment

Eliminates the need for retraining at runtime

🖥️ Implementation

The application is implemented using Streamlit, providing an interactive and user-friendly web interface.

🔹 Implementation Highlights

Clean text input for user reviews

Real-time sentiment prediction on button click

Probability-based prediction output

Minimal dark-themed UI using embedded HTML & CSS

Direct integration with the trained ML pipeline for inference

The backend strictly performs sentiment classification without fabricated explanations or artificial emotional metrics.

📂 Repository Structure
google-play-store-review-sentiment-analysis/
├── app.py
│   └── Streamlit web application
├── reviews_pipeline.pkl
│   └── Serialized TF-IDF + Logistic Regression pipeline
├── requirements.txt
│   └── Python dependencies
├── README.md
│   └── Project documentation
└── .gitignore
    └── Excludes virtual environments and cache files


This structure is minimal, clean, and deployment-ready.

🛠️ Tech Stack

Programming Language

Python 3.9+

Machine Learning & NLP

scikit-learn (TF-IDF, Logistic Regression, Pipelines)

joblib

Data Processing

pandas

Web Application

Streamlit

Frontend Styling

HTML & CSS

Deployment (Optional)

Streamlit Community Cloud

✅ Conclusion

The Google Play Store Review Sentiment Analysis project demonstrates a complete NLP-based machine learning workflow, emphasizing:

Correct text preprocessing

Pipeline-based modeling

Responsible evaluation

Clean and reliable deployment
