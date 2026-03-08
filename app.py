from flask import Flask, request, jsonify
from predict import detect_phishing

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Phishing Detection System Running"

@app.route("/detect", methods=["GET"])
def detect():

    url = request.args.get("url")

    if not url:
        return jsonify({"error": "URL parameter required"})

    result = detect_phishing(url)

    return jsonify({
        "url": url,
        "prediction": result
    })

if __name__ == "__main__":
    app.run(debug=True)
