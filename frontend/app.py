from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/countries")
def countries():
    return jsonify(
        requests.get("http://country-service:5001/countries").json()
    )

@app.route("/api/holidays")
def holidays():
    code = request.args.get("code")
    return jsonify(
        requests.get(
            f"http://holiday-service:5002/holidays?code={code}"
        ).json()
    )

app.run(host="0.0.0.0", port=5000)
