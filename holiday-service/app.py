from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/holidays/<code>")
def holidays(code):
    url = f"https://date.nager.at/api/v3/PublicHolidays/2024/{code}"
    res = requests.get(url, timeout=10)

    if res.status_code != 200:
        return jsonify([])

    data = res.json()
    return jsonify([
        {"date": h["date"], "name": h["localName"]}
        for h in data[:10]
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
