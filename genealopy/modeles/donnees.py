from datetime import datetime

from genealopy.app import db


class Authorship(db.Model):
    __tablename__ = "authorship"
    authorship_id = db.Column(db.Integer, nullable=True, autoincrement=True, primary_key=True)
    authorship_place_id = db.Column(db.Integer, db.ForeignKey('place.place_id'))
    authorship_user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    authorship_personnes_id = db.Column(db.Integer, db.ForeignKey('personnes.personne_id'))
    authorship_relation_id = db.Column(db.Integer, db.ForeignKey('relation.relation_id'))
    authorship_evenement_id = db.Column(db.Integer, db.ForeignKey('evenement.evenement_id'))
    authorship_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    user = db.relationship("User", back_populates="authorships")
    place = db.relationship("Place", back_populates="authorships")
    personnes = db.relationship("Personnes", back_populates="authorships")
    relation = db.relationship("relation", back_populates="authorships")
    evenement = db.relationship("evenement", back_populates="authorships")


class Personnes(db.Model):
    personne_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    personne_nom = db.Column(db.Text)
    personne_prenom = db.Column(db.Text)
    place_naissance_id = db.Column(db.Integer, db.ForeignKey('place.place_id'))
    place_mariage_id = db.Column(db.Integer, db.ForeignKey('place.place_id'))
    place_deces_id = db.Column(db.Integer, db.ForeignKey('place.place_id'))

    place = db.relationship("Place", back_populates="Personnes")
    evenement = db.relationship("Evenement", back_populates="Personnes")
    relation = db.relationship("Relation", back_populates="Personnes")
    user = db.relationship("User", back_populates="Personnes")
    authorships = db.relationship("Authorship", back_populates="Personnes")


class Place(db.Model):
    place_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    place_nom = db.Column(db.Text)
    place_pays = db.Column(db.Text)

    personnes = db.relationship("Personnes", back_populates="Place")
    evenement = db.relationship("Evenement", back_populates="Place")
    user = db.relationship("User", back_populates="Place")
    authorships = db.relationship("Authorship", back_populates="Place")


class Relation(db.Model):
    relation_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    relation_nom = db.Column(db.Text)
    relation_personne_1_id = db.Column(db.Integer, db.ForeignKey('personnes.personne_id'))
    relation_personne_2_id = db.Column(db.Integer, db.ForeignKey('personnes.personne_id'))

    personnes = db.relationship("Personnes", back_populates="Relation")
    evenement = db.relationship("Evenement", back_populates="Relation")


class Evenement(db.Model):
    evenement_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    evenement_nom = db.Column(db.Text)
    evenement_date = db.Column(db.Text)
    evenement_personne_id = db.Column(db.Integer, db.ForeignKey('personnes.personnes_id'))
    evenement_place_id = db.Column(db.Integer, db.ForeignKey('place.place_id'))

    personnes = db.relationship("Personnes", back_populates="Evenement")
    relation = db.relationship("Relation", back_populates="Evenement")
    place = db.relationship("Place", back_populates="Evenement")