from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/countries")
def countries():
    headers = {"User-Agent": "Mozilla/5.0"}
    url = "https://restcountries.com/v3.1/all?fields=name,capital,population,cca2,flags"
    data = requests.get(url, headers=headers).json()
    if not isinstance(data, list):
        return jsonify([]), 500
    
    # Turkiye'yi bul
    turkey = next((c for c in data if c["cca2"] == "TR"), None)
    
    result = []
    if turkey:
        result.append({
            "name": turkey["name"]["common"],
            "capital": turkey.get("capital", ["-"])[0],
            "population": turkey["population"],
            "code": turkey["cca2"],
            "flag": turkey["flags"]["png"]
        })
    
    for c in data[:10]:
        result.append({
            "name": c["name"]["common"],
            "capital": c.get("capital", ["-"])[0],
            "population": c["population"],
            "code": c["cca2"],
            "flag": c["flags"]["png"]
        })
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
