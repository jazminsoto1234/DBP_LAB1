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
        js.dump(dataAnime, archivo, indent=4)
    
    return dataAnime

@app.route("/anime/{<int:id_Anime>}", methods=['PUT'])
def UpdateAnime(id_Anime):
    for anime in dataAnime['anime']:
        if anime['id'] == id_Anime:
            #anime['id'] = request.json['id']
            anime['titulo'] = request.json['titulo']
            anime['puntaje'] = request.json['puntaje']
            anime['tipo'] = request.json['tipo']
            anime['season'] = request.json['season']
            anime['generos'] = request.json['generos']
        
            with open(r"C:\Users\HP\Desktop\DBP\TAREAS\anime.json", "w") as archivo: #Cargando archivo de escritura
                js.dump(dataAnime, archivo, indent=4) #Actualiza los datos
            return dataAnime
    return "No se encontro el anime :("


@app.route("/anime/{<int:id_Anime>}", methods= ['DELETE'])
def deleteAnime(id_Anime):
    for anime in dataAnime['anime']:
        if anime['id'] == id_Anime:
            dataAnime['anime'].remove(anime)
            with open(r"C:\Users\HP\Desktop\DBP\TAREAS\anime.json", "w") as archivo: #Cargando archivo de escritura
                js.dump(dataAnime, archivo, indent=4) #Actualiza los datos
            
            return dataAnime
    return "No se encontro el anime :("


if __name__ == "__main__":
    app.run(debug=True)