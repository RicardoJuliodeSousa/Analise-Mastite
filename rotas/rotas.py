from flask import Blueprint, request

cadastro = Blueprint('cadastro', __name__)

@cadastro.route('/cadstro', method='POST')
def cadastro(): 
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    confirmar_senha = request.form.get('confirme sua senha')
    regiao = request.form.get('de qual região você é?')

    if senha != confirmar_senha:
        return 'As senhas não coincidem. Por favor, tente novamente.'
    
    if"@gmail.com" not in email:
        return'o email é inválido. Por favor, tente outro'

    return 'Cadastro realizado com sucesso!'



login = Blueprint('login', __name__)

@login.route('/login', method = 'POST')
def login():
    email = request.form.get('email')
    senha = request.form.get('senha')

    if email == '' or senha == '':
        return 'Por favor, preencha todos os campos.'
    
    if email or senha != email.cadastro.route or senha.cadastro.route:
        return 'Email ou senha incorretos. Por favor, tente novamente.'
    
    if email == email.cadastro.route and senha == senha.cadastro.route:
        return'Login bem-sucedido! Bem-vindo de volta!'