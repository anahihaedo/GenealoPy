from ...app import db


class Personnes(db.Model):
    personne_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    personne_nom = db.Column(db.Text)
    personne_prenom = db.Column(db.Text)


class Place(db.Model):
    place_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    place_ville = db.Column(db.Text)
    place_pays = db.Column(db.Text)

    # Je ne sais pas si je veux garder latitute et etc, comme info.


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

    class User(db.Model):
        user_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
        user_nom = db.Column(db.Text, nullable=False)
        user_login = db.Column(db.String(45), nullable=False)
        user_email = db.Column(db.Text, nullable=False)
        user_password = db.Column(db.String(64), nullable=False)
