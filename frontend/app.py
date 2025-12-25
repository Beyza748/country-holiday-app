from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)

COUNTRY_SERVICE = "http://country-service:5001"
HOLIDAY_SERVICE = "http://holiday-service:5002"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/countries")
def api_countries():
    try:
        r = requests.get(f"{COUNTRY_SERVICE}/countries", timeout=10)
        return jsonify(r.json())
    except:
        return jsonify({"error": "Country service unreachable"}), 500

@app.route("/api/holidays")
def api_holidays():
    code = request.args.get("code")
    try:
        r = requests.get(f"{HOLIDAY_SERVICE}/holidays/{code}", timeout=10)
        return jsonify(r.json())
    except:
        return jsonify({"error": "Holiday service unreachable"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
