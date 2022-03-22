from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask("Nom")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pythonProjects/db.sqlite'
db = SQLAlchemy(app)

#import os

#chemin_actuel = os.path.dirname(os.path.abspath(__file__))
#templates = os.path.join(chemin_actuel, "templates")
#statics = os.path.join(chemin_actuel, "static")

#app = Flask(
#"Application",
#template_folder=templates,
#static_folder=statics)

class Personnes(db.Model):
    personne_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    personne_nom = db.Column(db.Text)
    personne_prenom = db.Column(db.Text)


class Place(db.Model):
    place_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    place_ville = db.Column(db.Text)
    place_pays = db.Column(db.Text)

    #Je ne sais pas si je veux garder latitute et etc, comme info.

class Relation_personnes(db.Model):
    relation_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    relation_nom = db.Column(db.Text)

 class Relation_ville(db.Model):
        relation_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
        naissance_ville = db.Column(db.Text)
        naissance_pays = db.Column(db.Text)
        mariage_ville = db.Column(db.Text)
        mariage_pays = db.Column(db.Text)
        deces_ville = db.Column(db.Text)
        deces_pays = db.Column(db.Text)

class Evenement(db.Model):
    evenement_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    evenement = db.Column(db.Text)

    class Date(db.Model):
        date_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
        dates = db.Column(db.Text)
        personne_evenement = db.Column(db.Text)

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
