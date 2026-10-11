# Sentiment Analysis Web Application

## 📌 Project Overview
This project is a web-based Sentiment Analysis application that analyzes text and classifies it as **Positive** or **Negative**. It also provides a confidence score for the prediction.

## ✨ Features
- Predicts positive and negative sentiment.
- Displays a confidence score for each prediction.
- Simple web interface for entering text.
- Built using Flask and a pre-trained Transformer model.
- Includes Docker support for containerization.

## 🛠️ Technologies Used
- **Python** – Application logic
- **Flask** – Backend web framework
- **Hugging Face Transformers** – Sentiment analysis pipeline
- **DistilBERT** – Pre-trained sentiment classification model
- **HTML** – User interface
- **Docker** – Containerization

## ⚙️ Installation and Setup

### 1. Clone the repository
```bash
git clone https://github.com/saginalakavyasree05-debug/Sentiment-Analysis-Project.git
cd Sentiment-Analysis-Project
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the application
```bash
python app.py
```

### 4. Open the application
Visit `http://localhost:7860` in your browser.

**Note:** The first run may download the pre-trained model, so an internet connection is required.

## 🤖 Model Information
The application uses `distilbert-base-uncased-finetuned-sst-2-english`, a DistilBERT model fine-tuned on the Stanford Sentiment Treebank (SST-2) dataset for binary sentiment classification.

## ⚠️ Limitations
- The model is designed for English text.
- It predicts positive or negative sentiment, which may not capture neutral or mixed opinions.
- Inputs that are not meaningful reviews may still receive a prediction.

## 👩‍💻 Author
Kavya

## 📸 Project Screenshot
positive
![Sentiment Analysis Demo](sentiment-analysis-demo.png)
negative
![Sentiment Analysis Demo](sentiment-analysis-demo1.png)
