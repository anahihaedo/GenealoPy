from warnings import warn

LIEUX_PAR_PAGE = 2
SECRET_KEY = "BLABLABLA !"

if SECRET_KEY == "JE SUIS UN SECRET!":
    warn("Le secret par défaut n'a pas été changé, vous devriez le faire", Warning)

"""
class _TEST:
    SECRET_KEY = SECRET_KEY
    # On configure la base de données
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Je ne sais pas qu'est que c'est ça

class _PRODUCTION:
    SECRET_KEY = SECRET_KEY
    # On configure la base de données
    # SQLALCHEMY_DATABASE_URI = 'mysql://genealopy_user:password@localhost/genealopy'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


CONFIG = {
    "test": _TEST,
    "production": _PRODUCTION
}
"""

def templates():
    return None