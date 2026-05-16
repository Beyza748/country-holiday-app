from flask import Flask, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

@app.route("/holidays")
def holidays():
    code = request.args.get("code")
    year = datetime.now().year
    try:
        response = requests.get(f"https://date.nager.at/api/v3/PublicHolidays/{year}/{code}")
        data = response.json()
        if not isinstance(data, list):
            return jsonify([{"date": "-", "name": "Bu ulke icin tatil bilgisi bulunamadi"}])
        return jsonify([{"date": h["date"], "name": h["localName"]} for h in data[:5]])
    except:
        return jsonify([{"date": "-", "name": "Bilgi alinamiyor"}])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
