from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/countries")
def countries():
    data = requests.get("https://restcountries.com/v3.1/all").json()

    result = []
    for c in data[:10]:
        result.append({
            "name": c["name"]["common"],
            "capital": c.get("capital", ["-"])[0],
            "population": c["population"],
            "code": c["cca2"],
            "flag": c["flags"]["png"]
        })

    return jsonify(result)

app.run(host="0.0.0.0", port=5001)
