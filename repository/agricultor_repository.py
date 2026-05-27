from extensao import bd
from Models.Agricultor import Agricultor

class AgricultorRepository:
    def buscar_por_email_e_senha(self, email, senha):
        return Agricultor.query.filter_by(email=email, senha=senha).first()
    
    def salvar(self, agricultor):
        try:

            bd.session.add(agricultor)
            bd.session.commit()
            return True
    
        except Exception as e:
            print(f'Erro ao salvar agricultor: {e}')
            bd.session.rollback()
            return False
        

        def listar_todos(self):
            return Agricultor.query.all()