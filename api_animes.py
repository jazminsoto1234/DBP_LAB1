from flask import Flask, request
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

@app.route("/anime", methods= ['POST'])
def addAnime():
    anime = { #Que solo aceptara este formato y lo que el cliente añada de mas no lo tomara en cuenta
        "id": request.json['id'],
        "titulo": request.json['titulo'],
        "puntaje": request.json['puntaje'],
        "tipo": request.json['tipo'],
        "season": request.json['season'],
        "generos": request.json['generos'],
    }
    dataAnime['anime'].append(anime)
    with open(r"C:\Users\HP\Desktop\DBP\TAREAS\anime.json", 'w') as archivo: #Abriendo archivo json para escritura
        js.dump(dataAnime, archivo)
    
    return dataAnime

if __name__ == "__main__":
    app.run(debug=True)