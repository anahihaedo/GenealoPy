from warnings import warn

LIEUX_PAR_PAGE = 2
SECRET_KEY = "BLABLABLA !"

if SECRET_KEY == "JE SUIS UN SECRET !":
    warn("Le secret par défaut n'a pas été changé, vous devriez le faire", Warning)


def templates():
    return None


def statics():
    return None
