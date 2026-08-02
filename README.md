# Phishing Link Detector

An AI-powered tool that detects phishing URLs using Machine Learning. The project analyzes URL and website content features to classify links as **phishing** or **legitimate**, helping flag malicious links before users interact with them.

## Problem

Phishing attacks remain one of the most common cyberattack vectors, tricking users into revealing sensitive information through fake websites that closely mimic legitimate ones. This project explores how Machine Learning can automate the detection of these malicious URLs.

## How It Works

1. **Data Collection** – Gathers a dataset of phishing and legitimate URLs [add source, e.g. PhishTank / UCI Phishing dataset].
2. **Feature Extraction** – Extracts URL-based and website content-based features (e.g. [list a few: URL length, use of "@" symbol, presence of HTTPS, domain age, etc.]).
3. **Model Training** – Trains a Machine Learning classification model ([name the algorithm you used, e.g. Random Forest / Logistic Regression / Decision Tree]) on the extracted features.
4. **Prediction** – Classifies a new URL as phishing or legitimate based on the trained model.

## Tech Stack

- Machine Learning: [scikit-learn / etc.]
- Data Processing: [pandas, numpy, etc.]
- [Add any other libraries/tools used]

##  Results

- Model accuracy: [add your accuracy score, e.g. 94%]
- [Add any comparison between models if you tested more than one]

##  Screenshots

### Home Page
![Home](assets/Home.png)

### Phishing Link Detected
![Phishing Result](assets/phishing-result.png)

### Legitimate Link Detected
![Legitimate Result](assets/legitimate-result.png)

## How to Run

```bash
# Clone the repository
git clone https://github.com/Malak-Alharbi/phishing-detector.git
cd phishing-detector

# Install dependencies
[pip install -r requirements.txt]

# Run the project
[python main.py]
```

##  Project Structure

```
phishing-detector/
├── [data/]              # Dataset files
├── [notebooks/]         # Model training / experimentation
├── [src/]                # Core detection logic
└── README.md
```

## Future Improvements

- Expand the dataset for better generalization
- Test additional ML models and compare performance
- Deploy as a browser extension or web app for real-time detection

## Author

**Malak Alharbi**
Information Systems Graduate | Cybersecurity Enthusiast
[LinkedIn](https://www.linkedin.com/in/malak-alharbi-is) · [GitHub](https://github.com/Malak-Alharbi)
