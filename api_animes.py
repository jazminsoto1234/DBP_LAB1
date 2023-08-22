from flask import Flask
import json as js

app = Flask(__name__)
dataAnime = js.load(open(r"C:\Users\HP\Desktop\DBP\TAREAS\anime.json"))

@app.route("/anime")
def getAnimes():
    return dataAnime

@app.route("/anime/{<int:id_Anime>}")
def getAnime(id_Anime):
    for anime in dataAnime['anime']:
        if anime['id'] == id_Anime:
            return anime
    return "No se encontro el anime :("


if __name__ == "__main__":
    app.run(debug=True)