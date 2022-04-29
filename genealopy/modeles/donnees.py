import datetime
from sqlalchemy import and_, or_

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
    relation = db.relationship("Relation", back_populates="authorships")
    evenement = db.relationship("evenement", back_populates="authorships")


class Personnes(db.Model):
    __tablename__ = "personnes"
    personne_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    personne_nom = db.Column(db.Text)
    personne_prenom = db.Column(db.Text)

    evenement = db.relationship("evenement", back_populates="personnes")
    # relation = db.relationship("Relation", back_populates="personnes")
    authorships = db.relationship("Authorship", back_populates="personnes")


class Place(db.Model):
    __tablename__ = "place"
    place_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    place_nom = db.Column(db.Text)
    place_pays = db.Column(db.Text)

    evenement = db.relationship("evenement", back_populates="place")
    authorships = db.relationship("Authorship", back_populates="place")


class evenement(db.Model):
    __tablename__ = "evenement"
    evenement_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    evenement_nom = db.Column(db.Text)
    evenement_date = db.Column(db.Text)
    evenement_personne_id = db.Column(db.Integer, db.ForeignKey('personnes.personne_id'))
    id_evenement_place = db.Column(db.Integer, db.ForeignKey('place.place_id'))

    personnes = db.relationship("Personnes", back_populates="evenement")
    # relation = db.relationship("Relation", back_populates="evenement")
    place = db.relationship("Place", back_populates="evenement")
    authorships = db.relationship("Authorship", back_populates="evenement")


class Relation(db.Model):
    __tablename__ = "relation"
    relation_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    relation_nom = db.Column(db.Text)
    relation_personne_1_id = db.Column(db.Integer, db.ForeignKey('personnes.personne_id'))
    relation_personne_2_id = db.Column(db.Integer, db.ForeignKey('personnes.personne_id'))

    personne_1 = db.relationship("Personnes", foreign_keys=[relation_personne_1_id],
                                 backref="relation_personne_1")
    personne_2 = db.relationship("Personnes", foreign_keys=[relation_personne_2_id],
                                 backref="relation_personne_2")
    # evenement = db.relationship("evenement", back_populates="relation")
    authorships = db.relationship("Authorship", back_populates="relation")
