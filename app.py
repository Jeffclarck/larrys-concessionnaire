from flask import Flask, request, jsonify, send_from_directory
import json
import os

app = Flask(__name__, static_folder='static')

JSON_FILE = "vehicules.json"

def generate_fiches():
    from pathlib import Path
    os.makedirs("vehicules", exist_ok=True)
    with open(JSON_FILE, "r", encoding="utf-8") as f:
        vehicules = json.load(f)
    for v in vehicules:
        filename = v['name'].lower().replace(" ", "-") + ".html"
        path = Path("vehicules") / filename
        html = f"""<!DOCTYPE html>
<html lang='fr'><head><meta charset='UTF-8'>
<title>{v['name']} - Fiche</title></head><body>
<h1>{v['name']}</h1><p>Catégorie : {v['category']}</p>
<p>Prix : {v['price']}</p><p>Carte grise : {v['carte_grise']}</p>
<p>Performance : {v['performance']}</p><p>Date : {v['date']}</p>
<a href='../index.html'>Retour</a></body></html>"""
        with open(path, "w", encoding="utf-8") as out:
            out.write(html)

@app.route("/")
def serve_form():
    return send_from_directory("static", "interface.html")

@app.route("/add", methods=["POST"])
def add_vehicle():
    data = request.json
    vehicules = []
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            vehicules = json.load(f)
    vehicules.append(data)
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(vehicules, f, indent=2, ensure_ascii=False)
    generate_fiches()
    return jsonify({"message": "✅ Véhicule ajouté."}), 200

if __name__ == "__main__":
    app.run(debug=True)
