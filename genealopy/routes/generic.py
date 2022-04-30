from flask import render_template, request, flash, redirect
from flask_login import current_user, login_user, logout_user, login_required

from ..app import app, login
from ..constantes import LIEUX_PAR_PAGE, PERSONNES_PAR_PAGE, RESULTATS_PAR_PAGES_INDEX, RESULTATS_PAR_PAGES
from ..modeles.donnees import *
from ..modeles.utilisateur import *

from sqlalchemy import and_, or_


@app.route("/")
def homepage():
    """ Route permettant l'affichage d'une page accueil
    """
    return render_template("pages/homepage.html")


@app.route("/index")
def base():
    return render_template("pages/index.html")

@app.route("/index_person")
def index_person():
    page = request.args.get("page", 1)
    if isinstance(page, str) and page.isdigit():
        page = int(page)
    else:
        page = 1

    personnes = Personnes.query.order_by(Personnes.personne_nom).paginate(page=page, per_page=RESULTATS_PAR_PAGES_INDEX)
    return render_template("pages/person_index.html", personnes=personnes)

@app.route("/index_place")
def index_place():
    page = request.args.get("page", 1)
    if isinstance(page, str) and page.isdigit():
        page = int(page)
    else:
        page = 1

    place = Place.query.order_by(Place.place_nom).paginate(page=page, per_page=RESULTATS_PAR_PAGES_INDEX)
    return render_template("pages/index_place.html", place=place)

@app.route("/index_even")
def index_even():
    page = request.args.get("page", 1)
    if isinstance(page, str) and page.isdigit():
        page = int(page)
    else:
        page = 1

    evenem = evenement.query.order_by(evenement.evenement_nom).paginate(page=page, per_page=RESULTATS_PAR_PAGES_INDEX)
    return render_template("pages/index_even.html", evenem=evenem)

@app.route("/person/<int:personne_id>")
def person(personne_id):
    """Création d'une page de contenu pour une personne.
        :param personne_id: Id de la clé primaire de la table Personnes dans la base de données
        :type personne_id: Integer
        :returns: création de la page grâce au render_template """

    personne_unique = Personnes.query.get(personne_id)
    return render_template("pages/person.html", person=personne_unique)

@app.route("/even/<int:evenement_id>")
def even(evenement_id):

    unique_even = evenement.query.get(evenement_id)
    return render_template("pages/even.html", nom="Genealopy", even=unique_even)


@app.route("/place/<int:place_id>")
def lieu(place_id):
    """ Route permettant l'affichage des données d'un lieu

    :param place_id: Identifiant numérique du lieu
    """
    # On a bien sûr aussi modifié le template pour refléter le changement
    unique_lieu = Place.query.get(place_id)
    return render_template("pages/place.html", nom="Genealopy", lieu=unique_lieu)


@app.route("/recherche")
def recherche():
    """ Route permettant la recherche plein-texte
    """
    # On préfèrera l'utilisation de .get() ici
    #   qui nous permet d'éviter un if long (if "clef" in dictionnaire and dictonnaire["clef"])
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
        resultats = Personnes.query.filter(
                or_(
                Personnes.personne_nom.like("%{}%".format(motclef)),
                Personnes.personne_prenom.like("%{}%".format(motclef)),
                Personnes.personne_id.like("%{}%".format(motclef))
                )
        ) \
            .paginate(page=page, per_page=RESULTATS_PAR_PAGES)
        titre = "Résultat pour la recherche '" + motclef + "'"
    return render_template("pages/recherche.html", resultats=resultats, titre=titre, keyword=motclef)

@app.route("/ajout_person", methods=["GET", "POST"])
@login_required
def ajout_person():

    # Ajout d'une personne
    if request.method == "POST":
        statut, informations = Personnes.ajout_personne(
        ajout_person_id = request.form.get("ajout_person_id", None),
        ajout_person_nom = request.form.get("ajout_person_nom", None),
        ajout_person_prenom = request.form.get("ajout_person_prenom", None)
        )

        if statut is True:
            flash("Ajouter une nouvelle personne", "success")
            return redirect("/")
        else:
            flash("L'ajout a échoué pour les raisons suivantes : " + ", ".join(informations), "danger")
            return render_template("pages/ajout_person.html")
    else:
        return render_template("pages/ajout_person.html")

@app.route("/ajout_place", methods=["GET", "POST"])
@login_required
def ajout_place():

    # Ajout d'une personne
    if request.method == "POST":
        statut, informations = Place.ajout_place(
        ajout_place_id = request.form.get("ajout_place_id", None),
        ajout_place_nom = request.form.get("ajout_place_nom", None),
        ajout_place_pays = request.form.get("ajout_place_pays", None)
        )

        if statut is True:
            flash("Ajouter une nouvelle ville", "success")
            return redirect("/")
        else:
            flash("L'ajout a échoué pour les raisons suivantes : " + ", ".join(informations), "danger")
            return render_template("pages/ajout_place.html")
    else:
        return render_template("pages/ajout_place.html")


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


@app.route("/supprimer_person/<int:personne_id>", methods=["POST", "GET"])
@login_required
def supprimer_person(personne_id):
    suppr_person = Personnes.query.get(personne_id)

    if request.method == "POST":
        statut = Personnes.supprimer_person(
            personne_id=personne_id
        )

        if statut is True:
            flash("Suppression réussie", "success")
            return redirect("/")
        else:
            flash("La suppression a échoué. Réessayez !", "error")
            return redirect("/")
    else:
        return render_template("pages/supprimer_person.html", suppr_person=suppr_person)

@app.route("/supprimer_place/<int:place_id>", methods=["POST", "GET"])
@login_required
def supprimer_place(place_id):
    suppr_place = Place.query.get(place_id)

    if request.method == "POST":
        statut = Place.supprimer_person(
            place_id=place_id
        )

        if statut is True:
            flash("Suppression réussie", "success")
            return redirect("/")
        else:
            flash("La suppression a échoué. Réessayez !", "error")
            return redirect("/")
    else:
        return render_template("pages/supprimer_place.html", suppr_place=suppr_place)



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

@app.route("/browse")
def browse():
    """ Route permettant la recherche plein-texte
    """
    # On préfèrera l'utilisation de .get() ici
    #   qui nous permet d'éviter un if long (if "clef" in dictionnaire and dictonnaire["clef"])
    page = request.args.get("page", 1)

    if isinstance(page, str) and page.isdigit():
        page = int(page)
    else:
        page = 1

    resultats = Place.query.paginate(page=page, per_page=LIEUX_PAR_PAGE)

    return render_template(
        "pages/browse.html",
        resultats=resultats
    )