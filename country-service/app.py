from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/countries")
def countries():
    res = requests.get("https://restcountries.com/v3.1/all", timeout=10)
    data = res.json()

    output = []
    for c in data[:20]:
        output.append({
            "code": c["cca2"],
            "name": c["name"]["common"],
            "capital": c.get("capital", ["-"])[0],
            "population": c["population"],
            "flag": c["flags"]["png"]
        })

    return jsonify(output)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
