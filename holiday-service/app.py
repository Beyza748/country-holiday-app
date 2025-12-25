from flask import Flask, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

@app.route("/holidays")
def holidays():
    code = request.args.get("code")
    year = datetime.now().year

    data = requests.get(
        f"https://date.nager.at/api/v3/PublicHolidays/{year}/{code}"
    ).json()

    return jsonify([
        {"date": h["date"], "name": h["localName"]}
        for h in data[:5]
    ])

app.run(host="0.0.0.0", port=5002)
