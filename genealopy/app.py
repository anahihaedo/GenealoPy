import os
from flask import Flask

from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# from .constantes import CONFIG
from .constantes import SECRET_KEY

chemin_actuel = os.path.dirname(os.path.abspath(__file__))
templates = os.path.join(chemin_actuel, "templates")
statics = os.path.join(chemin_actuel, "static")

app = Flask(
    "Genealopy",
    template_folder=templates,
    static_folder=statics
)

# configuration de l'application: secret, base de données, login manager
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db: object = SQLAlchemy(app)
login = LoginManager(app)

"""
# On initie l'extension
db = SQLAlchemy()
# On met en place la gestion d'utilisateur-rice-s
login = LoginManager()
"""


"""
def config_app(config_name="test"):
    # Create the application
    app.config.from_object(CONFIG[config_name])

    # Set up extensions
    db.init_app(app)
    # assets_env = Environment(app)
    login.init_app(app)

    # Register Jinja template functions

    return app
"""


def run(debug: object) -> object:
    """

    :rtype: object
    """
    return None


from .routes.generic import *
