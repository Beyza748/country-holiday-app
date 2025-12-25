from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/countries")
def countries():
    try:
        r = requests.get(
            "https://restcountries.com/v3.1/all",
            timeout=5
        )
        r.raise_for_status()
        data = r.json()

        result = []
        for c in data[:20]:
            result.append({
                "code": c["cca2"],
                "name": c["name"]["common"],
                "capital": c.get("capital", ["-"])[0],
                "population": c["population"],
                "flag": c["flags"]["png"]
            })
        return jsonify(result)

    except Exception:
        # 🔥 FALLBACK – HER ZAMAN ÇALIŞIR
        return jsonify([
            {
                "code": "TR",
                "name": "Turkey",
                "capital": "Ankara",
                "population": 85000000,
                "flag": "https://flagcdn.com/w320/tr.png"
            },
            {
                "code": "DE",
                "name": "Germany",
                "capital": "Berlin",
                "population": 83000000,
                "flag": "https://flagcdn.com/w320/de.png"
            }
        ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

