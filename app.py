from flask import Flask, render_template
import os

chemin_actuel = os.path.dirname(os.path.abspath(__file__))
templates = os.path.join(chemin_actuel, "templates")
statics = os.path.join(chemin_actuel, "static")

app = Flask(
    "Application",
    template_folder=templates,
    static_folder=statics)


@app.route("/")
def homepage(lieux=None):
    return render_template("pages/homepage.html", nom="GenealoPy", lieux=lieux)


@app.route("/fonds")
def base():
    return render_template("pages/recherche_avancée.html")


@app.route("/place/<int:place_id>")
def lieu(place_id):
    return render_template("pages/place.html", nom="GenealoPy", lieu=lieux[place_id])



if __name__ == "__main__":
    app.run(debug=True)
