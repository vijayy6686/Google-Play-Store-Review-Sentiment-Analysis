import streamlit as st
import pickle
import time

# ===============================
# Page config
# ===============================
st.set_page_config(
    page_title="Google Play Store App Reviews Sentiment Analysis",
    page_icon="https://www.gstatic.com/android/market_images/web/play_prism_hlock_2x.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ===============================
# Global CSS
# ===============================
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top, #020617 0%, #000000 70%);
    color: #E5E7EB;
}

header, footer {visibility: hidden;}

.hero {
    background: linear-gradient(135deg, #6366F1, #7C3AED);
    border-radius: 24px;
    padding: 2.6rem 2rem;
    text-align: center;
    margin-bottom: 2.5rem;
}

.hero-title {
    font-size: 2.1rem;
    font-weight: 800;
    color: white;
}

.hero-sub {
    color: #E0E7FF;
    font-size: 0.95rem;
    margin-top: 0.4rem;
}

.section-title {
    font-size: 1.1rem;
    font-weight: 700;
    margin-bottom: 0.6rem;
}

.card {
    background: rgba(15, 23, 42, 0.95);
    border-radius: 18px;
    padding: 1.8rem;
    border: 1px solid rgba(255,255,255,0.06);
}

.stTextArea textarea {
    background: #020617;
    color: #F9FAFB;
    border-radius: 14px;
    border: 1px solid #374151;
}

.stButton > button {
    background: linear-gradient(135deg, #6366F1, #4F46E5);
    color: white;
    border-radius: 16px;
    height: 3.2rem;
    font-weight: 600;
    border: none;
}

.result-positive {
    background: rgba(34,197,94,0.18);
    color: #4ade80;
    padding: 1rem;
    border-radius: 14px;
    font-weight: 700;
    text-align: center;
}

.result-negative {
    background: rgba(239,68,68,0.18);
    color: #f87171;
    padding: 1rem;
    border-radius: 14px;
    font-weight: 700;
    text-align: center;
}

.result-neutral {
    background: rgba(234,179,8,0.18);
    color: #facc15;
    padding: 1rem;
    border-radius: 14px;
    font-weight: 700;
    text-align: center;
}

.confidence {
    font-size: 2.2rem;
    font-weight: 800;
}
</style>
""", unsafe_allow_html=True)

# ===============================
# Load trained pipeline
# ===============================
@st.cache_resource
def load_model():
    with open("reviews_pipeline.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()
# ===============================
# Text cleaning (CLOUD SAFE)
# ===============================
import re
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z\s]", " ", text)
    words = text.split()
    words = [w for w in words if w not in ENGLISH_STOP_WORDS]
    return " ".join(words)


# ===============================
# HERO
# ===============================
st.markdown("""
<div class="hero">
    <img src="https://www.gstatic.com/android/market_images/web/play_prism_hlock_2x.png" height="48">
    <div class="hero-title">Sentiment Analysis</div>
    <div class="hero-sub">Analyze Google Play Store reviews</div>
</div>
""", unsafe_allow_html=True)

# ===============================
# Layout
# ===============================
left, right = st.columns([3, 2], gap="large")

# ===============================
# LEFT: INPUT
# ===============================
with left:
    st.markdown("<div class='section-title'>Enter Your Review</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    review_text = st.text_area(
        "User Review",
        height=160,
        placeholder="Type your Google Play review here...",
        label_visibility="collapsed"
    )

    analyze = st.button("Analyze Sentiment", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ===============================
# RIGHT: RESULT
# ===============================
with right:
    st.markdown("<div class='section-title'>Analysis Result</div>", unsafe_allow_html=True)

    if analyze and review_text.strip():
        with st.spinner("Analyzing sentiment..."):
            time.sleep(0.3)

            pred = model.predict([review_text])[0]
            proba = model.predict_proba([review_text])[0]
            confidence = max(proba) * 100

            st.markdown("<div class='card'>", unsafe_allow_html=True)

            if pred == "Positive":
                st.markdown("<div class='result-positive'>Positive Review</div>", unsafe_allow_html=True)
            elif pred == "Neutral":
                st.markdown("<div class='result-neutral'>Neutral Review</div>", unsafe_allow_html=True)
            else:
                st.markdown("<div class='result-negative'>Negative Review</div>", unsafe_allow_html=True)

            st.markdown("<span style='color:#9CA3AF;'>Prediction Confidence</span>", unsafe_allow_html=True)
            st.markdown(f"<div class='confidence'>{confidence:.1f}%</div>", unsafe_allow_html=True)

            st.markdown("</div>", unsafe_allow_html=True)

