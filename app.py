import streamlit as st
import joblib
import pandas as pd
import re
from ssl_checker import check_ssl_certificate
from urllib.parse import urlparse


st.set_page_config(page_title="AI Phishing Link Detector", page_icon="🛡️", layout="centered")

model = joblib.load('phishing_model.pkl')


trusted_domains = [
    'google.com', 'microsoft.com', 'apple.com', 'amazon.com',
    'stc.com.sa', 'alrajhibank.com.sa', 'spa.gov.sa', 'moi.gov.sa',
    'linkedin.com', 'github.com'
]

def is_trusted_domain(url):
    try:
        domain = urlparse(url).netloc.replace('www.', '')
        return 1 if domain in trusted_domains else 0
    except Exception:
        return 0


def extract_features(url):
    features = {}
    features['url_length'] = len(url)
    features['has_at_symbol'] = 1 if '@' in url else 0
    features['has_ip'] = 1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0
    features['num_dots'] = url.count('.')
    features['has_https'] = 1 if url.startswith('https') else 0
    features['num_hyphens'] = url.count('-')
    features['has_valid_ssl'] = check_ssl_certificate(url)
    features['is_trusted_domain'] = is_trusted_domain(url)
    return features

st.title("🛡️ AI Phishing Link Detector")
st.write("Enter a URL below to check if it's safe or a phishing attempt.")

url_input = st.text_input("Enter the URL to check:", placeholder="https://example.com")


if st.button("🔍 Check URL"):
    if url_input:
        with st.spinner("Checking SSL certificate and analyzing URL..."):
            features = extract_features(url_input)
            features_df = pd.DataFrame([features])
            prediction = model.predict(features_df)[0]
            probability = model.predict_proba(features_df)[0]
            confidence = max(probability) * 100

        st.write("---")

        if prediction == "phishing":
            st.error(f"⚠️ *Phishing Detected*")
        else:
            st.success(f"✅ *Safe Link*")

        st.write(f"*Confidence:* {confidence:.1f}%")

        st.write("### Why this result?")
        st.write(f"- URL Length: {features['url_length']} characters")
        st.write(f"- Uses HTTPS: {'Yes' if features['has_https'] else 'No'}")
        st.write(f"- Valid SSL Certificate: {'Yes ✓' if features['has_valid_ssl'] else 'No ✗'}")
        st.write(f"- Known Trusted Domain: {'Yes ✓' if features['is_trusted_domain'] else 'No'}")
        st.write(f"- Contains IP address: {'Yes' if features['has_ip'] else 'No'}")
        st.write(f"- Number of hyphens: {features['num_hyphens']}")
        st.write(f"- Number of dots: {features['num_dots']}")
    else:
        st.warning("Please enter a URL first.")