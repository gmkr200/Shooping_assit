# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from scraper import extract_price_and_title

app = Flask(__name__)
CORS(app)

@app.route("/api/price-check", methods=["POST"])
def price_check():
    data = request.json
    url = data.get("url")
    selector = data.get("price_selector")

    if not url or not selector:
        return jsonify({"success": False, "error": "Missing url or price_selector"}), 400

    result = extract_price_and_title(url, selector)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
