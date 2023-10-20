from flask import Blueprint, request
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'models'))
from usuario import usuario_obj
# from analise_socket import analise_socket_obj

home = Blueprint('home', __name__)

@home.route('/api/cadastrar', methods=['POST'])
def cadastrar():

    token = usuario_obj.cadastrar(request.form)
    
    if token == False:
        return retornoAPI(400, 'USER_EXISTS', 'Usuário já cadastrado.')    

    return retornoAPI(200, 'success', token)


@home.route('/api/login', methods=['POST'])
def login():

    token = usuario_obj.login(request.form['usuario'], request.form['senha'])
    
    if token == False:
        return retornoAPI(400, 'USER_PASSWORD_WRONG', 'Usuário ou senha incorretos. Tente novamente.')    

    return retornoAPI(200, 'success', token)


@home.route('/api/status')
def status():

    jwt = request.cookies.get('guardian.jwt')

    if jwt != usuario_obj.jwt:
        return retornoAPI(404, 'USER_NOT_LOGGED', 'Usuário não logado.')    

    return retornoAPI(200, 'success', '')


def retornoAPI(status_code, status, dados):
    return {
        'status_code': status_code,
        'status': status,
        'data': dados
    }