from flask import Flask
import json as js

app = Flask(__name__)
dataAnime = js.load(open(r"C:\Users\HP\Desktop\DBP\TAREAS\anime.json"))

@app.route("/anime")
def getAnimes():
    return dataAnime

if __name__ == "__main__":
    app.run(debug=True)