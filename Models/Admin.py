from extensao import bd
from flask_login import UserMixin

class Admin(bd.Model, UserMixin):
    __tablename__ = 'admin'
    id = bd.column(bd.integer, primary_key=True)
    nome_admin = bd.column(bd.string(100), nullable=False)
    email_admin = bd.column(bd.string(100), unique=True, nullable=False)
    contribuicoes = bd.relationship('Contribuicao', backref='admin', lazy=True)

    def __repr__(self):
        return f'<Id: {self.id}, Admin: {self.nome_admin}, Email: {self.email_admin}>'
    @property
    def is_admin(self):
        return True
    
    def get_id(self):
        return f'admin_{self.id}'