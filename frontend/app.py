from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)

COUNTRY = "http://country-service:5001"
HOLIDAY = "http://holiday-service:5002"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/countries")
def api_countries():
    r = requests.get(f"{COUNTRY}/countries")
    return jsonify(r.json())

@app.route("/api/holidays")
def api_holidays():
    code = request.args.get("code")
    r = requests.get(f"{HOLIDAY}/holidays/{code}")
    return jsonify(r.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
