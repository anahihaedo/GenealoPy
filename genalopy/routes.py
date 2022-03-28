from flask import render_template

from .modeles.donnees import *
from .app import app, db


# from .modeles.donnees import Place


@app.route("/")
def homepage():
    if Place.query.get(1):
        print("y")
    else:
        print("n")
    lieux = Place.query.all()
    return render_template("pages/homepage.html", nom="GenealoPy", lieux=lieux)


@app.route("/fonds")
def base():
    return render_template("pages/recherche_avancée.html")


@app.route("/place/<int:place_id>")
def lieu(place_id):
    # On a bien sûr aussi modifié le template pour refléter le changement
    unique_lieu = Place.query.get(place_id)
    return render_template("pages/place.html", nom="GenealoPy", lieu=unique_lieu)
