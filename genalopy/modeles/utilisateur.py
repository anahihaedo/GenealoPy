from ..app import login, db

class User(db.Model):
    user_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    user_nom = db.Column(db.Text, nullable=False)
    user_login = db.Column(db.String(45), nullable=False)
    user_email = db.Column(db.Text, nullable=False)
    user_password = db.Column(db.String(64), nullable=False)

    def get_id(self):
        return self.id

# récupérer l'id de l'utilisateur.ice courant.e et gérer les connexions actives

@login.user_loader  # IL Y A UNE ERREUR A CET ENDROIT MAIS FUCK IF I KNOW WHY
def load_user(user_id):
    """Configurer l'user_loader: récupérer l'id de l'utilisateur.ice courant.e pour gérer les connexions actives.
    :param identifiant: l'identifiant de l'utilisateur.ice actuel.le
    :return: l'objet 'User' correspondant à cet identifiant
    """
    return User.query.get(int(user_id))
#@login_manager.user_loader
#def load_user(user_id):
#    return User.get(user_id)