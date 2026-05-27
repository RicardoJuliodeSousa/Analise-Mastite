from extensao import bd
from Models.Admin import Admin

class Admin_Repository:
    def __init__(self):
        self.bd = bd

    def verificar_login(self, email_admin, senha_admin):
        return Admin.query.filter_by(email_admin=email_admin, senha_admin=senha_admin).first()
    
    def cadastrar_admin(self, admin):
        try:
            self.bd.session.add(admin)
            self.bd.session.commit()
            return True
        
        except Exception as e:
            print(f'Erro ao cadastrar admin: {e}')
            self.bd.session.rollback()
            return False
        
    def listar_admins(self):
        return Admin.query.all()    