from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
#from flask_login import LoginManager
import os

from .constantes import SECRET_KEY, templates, statics, cartes

chemin_actuel = os.path.dirname(os.path.abspath(__file__))
templates = os.path.join(chemin_actuel, "templates")
statics = os.path.join(chemin_actuel, "static")

app = Flask(
"Application",
template_folder=templates,
static_folder=statics)

# configurer le secret
app.config['SECRET_KEY'] = SECRET_KEY
# configurer la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
# app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {"check_same_thread": False}
# initier l'extension de la bdd
db = SQLAlchemy(app)
# configurer la gestion d'utilisateur-rice-s
#login = LoginManager(app)

from.routes import lieu, homepage