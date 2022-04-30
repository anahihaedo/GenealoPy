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

    @staticmethod
    def ajout_person(ajout_person_id, ajout_person_nom, ajout_person_prenom):
        erreurs = []
        if not ajout_person_id:
            erreurs.append("Veuillez renseigner l'identifiant pour cette personne.")
        if not ajout_person_nom:
            erreurs.append(
                "Veuillez renseigner le nom de cette personne")
        if not ajout_person_prenom:
            erreurs.append(
                "Veuillez renseigner le prénom de cette personne")

            # S'il y a au moins une erreur, afficher un message d'erreur.
        if len(erreurs) > 0:
            return False, erreurs

            # Si aucune erreur n'a été détectée, ajout d'une nouvelle entrée dans la table AMendes (champs correspondant aux paramètres du modèle)
        nouvelle_personne = Personnes(personne_id=ajout_personnes_id,
                                      personne_nom=ajout_personnes_nom,
                                      personne_prenom=ajout_personnes_prenom)

        # Tentative d'ajout qui sera stoppée si une erreur apparaît.
        try:
            db.session.add(new_person)
            db.session.commit()
            return True, new_person

        except Exception as erreur:
            return False, [str(erreur)]

    # Méthode statique qui permet de supprimer une personne et qui est appelée dans la route correspondante.

    @staticmethod
    def supprimer_person(personne_id):

        suppr_person = Personnes.query.get(personne_id)

        try:
            db.session.delete(suppr_person)
            db.session.commit()
            return True

        except Exception as erreur:
            return False, [str(erreur)]


class Place(db.Model):
    __tablename__ = "place"
    place_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    place_nom = db.Column(db.Text)
    place_pays = db.Column(db.Text)

    evenement = db.relationship("evenement", back_populates="place")
    authorships = db.relationship("Authorship", back_populates="place")

    @staticmethod
    def ajout_person(ajout_place_id, ajout_place_nom, ajout_place_pays):
        erreurs = []
        if not ajout_place_id:
            erreurs.append("Veuillez renseigner l'identifiant du lieu.")
        if not ajout_place_nom:
            erreurs.append(
                "Veuillez renseigner la ville")
        if not ajout_place_pays:
            erreurs.append(
                "Veuillez renseigner le pays")

            # S'il y a au moins une erreur, afficher un message d'erreur.
        if len(erreurs) > 0:
            return False, erreurs


        nouveau_lieu = Place(place_id=ajout_place_id,
                                      place_nom=ajout_place_nom,
                                      place_pays=ajout_place_pays)

        # Tentative d'ajout qui sera stoppée si une erreur apparaît.
        try:
            db.session.add(new_place)
            db.session.commit()
            return True, new_place

        except Exception as erreur:
            return False, [str(erreur)]

    # Méthode statique qui permet de supprimer une personne et qui est appelée dans la route correspondante.

    @staticmethod
    def supprimer_place(place_id):

        suppr_place = Place.query.get(place_id)

        try:
            db.session.delete(suppr_place)
            db.session.commit()
            return True

        except Exception as erreur:
            return False, [str(erreur)]


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
