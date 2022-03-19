from flask import Flask, render_template

app = Flask("Application")

lieux = {
    0: {
        "nom": "Brésil",
        "ville": "Recife",
        "latlong": [-8.057838, -34.882897],
        "type": "pays",
        "description": "Brésil c'est le plus grand pays de l'Amérique du Sud."
                       "Recife c'est la capitale de l'Etat de Parnambuco, "
                       "dans le nord-est du pays."
    },
    1:
        {
            "nom": "Italia",
            "ville": "Stella",
            "type": "pays",
            "description": "L'Italie est un pays de l'Europe du Sud."
                           "Stella est une commune italienne de la province de Savone,"
                           "dans la région Ligurie en Italie.",
            "latlong": [44.393983, 8.495223]
        },
    2:

        {
            "nom": "Uruguay",
            "ville": "Montevideo",
            "type": "pays",
            "description": "La république orientale de l'Uruguay,"
                           "est un pays du Cône Sudde l’Amérique du Sud.",
            "latlong": [-34.901113, -56.164531]
        },
}


@app.route("/")
def homepage():
    return render_template("pages/homepage.html", nom="GenealoPy", lieux=lieux)


@app.route("/fonds")
def base():
    return render_template("pages/recherche_avancée.html")


@app.route("/place/<int:place_id>")
def lieu(place_id):
    return render_template("pages/place.html", nom="GenealoPy", lieu=lieux[place_id])


if __name__ == "__main__":
    app.run(debug=True)
