from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

bd = SQLAlchemy()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    from Models import Agricultor
    from Models import Admin

    try:
        tipo_usuario, id_numerico = user_id.split('_')
        id_numerico = int(id_numerico)

        if tipo_usuario == 'agricultor':
            return Agricultor.query.get(id_numerico)
        elif tipo_usuario == 'admin':
            return Admin.query.get(id_numerico)
        
    except ValueError:
        return None
    
    return None
