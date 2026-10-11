from flask import Flask, request, jsonify, send_from_directory
from transformers import pipeline

app = Flask(__name__, static_folder="static")

# Loaded once at startup (downloads the model the first time)
classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
)


@app.get("/")
def home():
    return send_from_directory("static", "index.html")


@app.post("/api/analyze")
def analyze():
    data = request.get_json(silent=True) or {}
    text = (data.get("text") or "").strip()
    if not text:
        return jsonify(error="Type a sentence first."), 400

    result = classifier(text[:512])[0]
    return jsonify(label=result["label"], score=round(result["score"], 4))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)