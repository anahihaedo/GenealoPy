from .modeles import donnees

LIEUX_PAR_PAGES = 2

from flask import render_template, request, flash, redirect
from flask_login import login_user, current_user, logout_user

from .app import app, login
from .modeles.donnees import Place, Personnes
from .modeles.utilisateur import User


@app.route("/")
def homepage():
    lieux = Place.query.order_by(Place.place_id.desc()).limit(3).all()
    return render_template("pages/homepage.html", nom="GenealoPy", lieux=lieux)


@app.route("/index")
def base():
    return render_template("/index.html")


@app.route("/index/personnes/")
def index_personnes(RESULTATS_PAR_PAGES_INDEX=None):
    page = request.args.get("page", 1)
    if isinstance(page, str) and page.isdigit():
        page = int(page)
    else:
        page = 1

    personnes = Personnes.query.order_by(Personnes.personne_nom).paginate(page=page, per_page=RESULTATS_PAR_PAGES_INDEX)
    return render_template("pages/Index_personnes.html", personnes=personnes)


@app.route("/index/place/")
def index_lieux(RESULTATS_PAR_PAGES_INDEX=None):
    page = request.args.get("page", 1)
    if isinstance(page, str) and page.isdigit():
        page = int(page)
    else:
        page = 1

    place = Place.query.order_by(Place.place_nom).paginate(page=page, per_page=RESULTATS_PAR_PAGES_INDEX)
    return render_template("pages/index_place.html", place=place)


@app.route("/personne/<int:personnes_id>")
def personne(personnes_id, personne_id=None):
    """Création d'une page de contenu pour une personne.
        :param personnes_id: Id de la clé primaire de la table Personnes dans la base de données
        :type personnes_id: Integer
        :returns: création de la page grâce au render_template """

    personne_unique = Personnes.query.filter(Personnes.personne_id == personne_id).first()
    return render_template("pages/personne.html", personne=personne_unique)


@app.route("/place/<int:place_id>")
def lieu(place_id):
    # On a bien sûr aussi modifié le template pour refléter le changement
    unique_lieu = Place.query.get(place_id)
    return render_template("pages/place.html", nom="GenealoPy", lieu=unique_lieu)


@app.route("/register", methods=["GET", "POST"])
def inscription():
    """ Route gérant les inscriptions
    """
    # Si on est en POST, cela veut dire que le formulaire a été envoyé
    if request.method == "POST":
        statut, donnees = User.creer(
            login=request.form.get("login", None),
            email=request.form.get("email", None),
            nom=request.form.get("nom", None),
            motdepasse=request.form.get("motdepasse", None)
        )
        if statut is True:
            flash("Enregistrement effectué. Identifiez-vous maintenant", "success")
            return redirect("/")
        else:
            flash("Les erreurs suivantes ont été rencontrées : " + ",".join(donnees), "error")
            return render_template("pages/inscription.html")
    else:
        return render_template("pages/inscription.html")


@app.route("/connexion", methods=["POST", "GET"])
def connexion():
    """ Route gérant les connexions
    """
    if current_user.is_authenticated is True:
        flash("Vous êtes déjà connecté-e", "info")
        return redirect("/")
    # Si on est en POST, cela veut dire que le formulaire a été envoyé
    if request.method == "POST":
        utilisateur = User.identification(
            login=request.form.get("login", None),
            motdepasse=request.form.get("motdepasse", None)
        )
        if utilisateur:
            flash("Connexion effectuée", "success")
            login_user(utilisateur)
            return redirect("/")
        else:
            flash("Les identifiants n'ont pas été reconnus", "error")

    return render_template("pages/connexion.html")


login.login_view = 'connexion'


@app.route("/deconnexion", methods=["POST", "GET"])
def deconnexion():
    if current_user.is_authenticated is True:
        logout_user()
    flash("Vous êtes déconnecté-e", "info")
    return redirect("/")


@app.route("/recherche")
def recherche():
    motclef = request.args.get("keyword", None)
    page = request.args.get("page", 1)

    if isinstance(page, str) and page.isdigit():
        page = int(page)
    else:
        page = 1

    # On crée une liste vide de résultat (qui restera vide par défaut
    #   si on n'a pas de mot clé)
    resultats = []

    # On fait de même pour le titre de la page
    titre = "Recherche"
    if motclef:
        resultats = Place.query.filter(
            Place.place_ville.like("%{}%".format(motclef))
        ).paginate(page=page, per_page=LIEUX_PAR_PAGES)
        titre = "Résultat pour la recherche `" + motclef + "`"

    return render_template(
        "pages/recherche.html",
        resultats=resultats,
        titre=titre,
        keyword=motclef
    )
