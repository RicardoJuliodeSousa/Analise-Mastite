from extensao import bd
from flask_login import UserMixin

class Agricultor(UserMixin, bd.Model):
    __tablename__ = 'agricultores'

    id = bd.column(bd.integer, primary_key=True)
    nome = bd.column(bd.string(100), nullable=False)
    email = bd.column(bd.string(100), unique=True, nullable=False)
    regiao = bd.column(bd.string(2, 25), nullable=False)

    def __repr__(self):
        return f'<Id: {self.id},Agricultor: {self.nome}, Email: {self.email}, Região: {self.regiao}>'
    
    @property
    def is_admin(self):
        return False
    
    def get_id(self):
        return f'agricultor_{self.ide}'
    
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "regiao": self.regiao
        }