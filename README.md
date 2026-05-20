# 📧 Email / SMS Spam Detection Classifier

> A machine learning-powered web application that classifies messages as **Spam** or **Not Spam** in real-time, built with Python, Scikit-learn, NLTK, and Streamlit.

---

## 🚀 Demo

Enter any email or SMS message into the app and instantly get a prediction:

- 🔴 **SPAM** — The message is flagged as spam
- 🟢 **NOT SPAM** — The message is safe

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [How It Works](#-how-it-works)
- [Installation](#-installation)
- [Usage](#-usage)
- [Dataset](#-dataset)
- [Model Details](#-model-details)
- [Contributing](#-contributing)
- [Author](#-author)

---

## 🧠 Overview

Spam messages are a major nuisance in digital communication — from promotional SMS blasts to phishing emails. This project tackles that problem using **Natural Language Processing (NLP)** and a **supervised machine learning** classifier trained on a labeled SMS/email dataset.

The model preprocesses raw text, converts it into numerical features using **TF-IDF vectorization**, and then makes a binary prediction using a trained classification model — all wrapped in an interactive **Streamlit** web app.

---

## ✨ Features

- Real-time spam classification for any email or SMS text
- Full NLP preprocessing pipeline (lowercasing → tokenization → stopword removal → stemming)
- Pre-trained model loaded from a serialized `.pkl` file for instant inference
- Clean, minimal Streamlit UI — no setup friction for end users
- Lightweight and easy to deploy

---

## 🛠 Tech Stack

| Category | Technology |
|---|---|
| Language | Python 3.x |
| Web Framework | Streamlit |
| ML Library | Scikit-learn |
| NLP | NLTK (punkt, stopwords, PorterStemmer) |
| Vectorization | TF-IDF (TfidfVectorizer) |
| Serialization | Pickle |
| Dataset | UCI SMS Spam Collection (`spam.csv`) |
| Notebook | Jupyter Notebook |

---

## 📁 Project Structure

```
Spam-detection-Classifier/
│
├── app.py                  # Streamlit web application
├── spam_detection.ipynb    # Jupyter Notebook — EDA, training & model building
├── spam.csv                # Dataset (SMS Spam Collection)
├── model.pkl               # Trained ML model (serialized)
├── vectorizer.pkl          # Fitted TF-IDF vectorizer (serialized)
└── requirements.txt        # Python dependencies
```

---

## ⚙️ How It Works

The application follows a standard NLP inference pipeline:

```
Raw Text Input
      │
      ▼
  Lowercase
      │
      ▼
  Tokenization  (NLTK word_tokenize)
      │
      ▼
  Filter alphanumeric tokens only
      │
      ▼
  Remove Stopwords & Punctuation
      │
      ▼
  Porter Stemming
      │
      ▼
  TF-IDF Vectorization  (pre-fitted vectorizer.pkl)
      │
      ▼
  ML Model Prediction  (model.pkl)
      │
      ▼
  Output: SPAM 🔴 / NOT SPAM 🟢
```

**Step-by-step breakdown:**

1. **Lowercasing** — Normalize all text to lowercase to reduce vocabulary size.
2. **Tokenization** — Split the message into individual words/tokens using NLTK.
3. **Alphanumeric Filtering** — Remove special characters and symbols that carry no semantic meaning.
4. **Stopword Removal** — Filter out common English filler words (e.g., "the", "is", "and") that don't distinguish spam from ham.
5. **Stemming** — Reduce words to their root form using the Porter Stemmer (e.g., "winning" → "win").
6. **TF-IDF Vectorization** — Convert the cleaned text into a numerical feature vector using the pre-fitted vectorizer.
7. **Model Prediction** — The trained classifier predicts 1 (Spam) or 0 (Not Spam).

---

## 📦 Installation

### Prerequisites

- Python 3.7 or above
- pip

### Steps

**1. Clone the repository**

```bash
git clone https://github.com/Vansh-pandey1/Spam-detection-Classifier.git
cd Spam-detection-Classifier
```

**2. (Optional) Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

The `requirements.txt` includes:
```
streamlit
nltk
scikit-learn
```

**4. Download NLTK data** (handled automatically by `app.py`, but you can pre-download manually)

```python
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
```

---

## ▶️ Usage

**Run the Streamlit app:**

```bash
streamlit run app.py
```

Then open your browser and go to `http://localhost:8501`.

1. Type or paste an email or SMS message into the text area.
2. Click the **Predict** button.
3. The app will display whether the message is **SPAM 🔴** or **NOT SPAM 🟢**.

### Example inputs to try

| Message | Expected Result |
|---|---|
| `Congratulations! You've won a FREE iPhone. Click here to claim now!` | 🔴 SPAM |
| `Hey, are we still on for dinner tonight?` | 🟢 NOT SPAM |
| `URGENT: Your bank account has been compromised. Call us immediately.` | 🔴 SPAM |
| `Can you send me the meeting notes from yesterday?` | 🟢 NOT SPAM |

---

## 📊 Dataset

The project uses the **UCI SMS Spam Collection Dataset** (`spam.csv`), a well-known benchmark dataset for spam classification tasks.

- **Total samples:** ~5,572 messages
- **Classes:** `ham` (not spam) and `spam`
- **Distribution:** ~87% ham, ~13% spam (imbalanced)
- **Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/sms+spam+collection)

---

## 🤖 Model Details

The model training and evaluation is documented in `spam_detection.ipynb`. The workflow includes:

- **Exploratory Data Analysis (EDA):** Understanding class distribution, message length analysis, and common words.
- **Feature Engineering:** TF-IDF vectorization of preprocessed text.
- **Model Training:** A classification algorithm (likely Naive Bayes — a strong baseline for text classification) trained on the vectorized features.
- **Serialization:** The trained model and vectorizer are saved as `model.pkl` and `vectorizer.pkl` using Python's `pickle` module for use in the web app.

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes and commit (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

### Ideas for improvement

- Add confidence scores / probability display
- Experiment with advanced models (Logistic Regression, SVM, BERT)
- Add support for bulk CSV file classification
- Deploy to Streamlit Cloud or Hugging Face Spaces
- Add a confusion matrix / accuracy display in the UI

---

## 👤 Author

**Vansh Pandey**

- GitHub: [@Vansh-pandey1](https://github.com/Vansh-pandey1)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

*Made with ❤️ and Python*
