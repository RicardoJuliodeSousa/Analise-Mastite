from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import login_required, login_user, logout_user

from repository.agricultor_repository import AgricultorRepository
from repository.admin_repository import AdminRepository

agricultor_dao = AgricultorRepository()
admin_dao = AdminRepository()


bp_agricultor = Blueprint('agricultor', __name__, url_prefix='/agricultor')


@bp_agricultor.route('/login', methods=['POST'])
def fazer_login_agricultor():
    email_login = request.form.get('usuario')
    senha = request.form.get('senha')

    agricultor = agricultor_dao.buscar_por_email(email_login)

    if agricultor and agricultor.verificar_email(email_login) and agricultor.verificar_senha(senha):
        login_user(agricultor)

        return redirect(url_for('homepage'))
    
    return render_template('login.html', error='Email ou senha incorretos. Por favor, tente novamente.')



@bp_agricultor.route('/cadastro', methods=['POST', 'GET'])
def cadastrar_agricultor():
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    confirmar_senha = request.form.get('confirmar_senha')
    regiao = request.form.get('regiao')

    if senha != confirmar_senha:
        return 'As senhas não coincidem. Por favor, tente novamente.'
    
    if"@gmail.com" not in email:
        return'o email é inválido. Por favor, tente outro'

    return 'Cadastro realizado com sucesso!'
