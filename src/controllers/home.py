from flask import Blueprint, request
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'models'))
from usuario import usuario_obj
from analise_socket import analise_socket_obj

home = Blueprint('home', __name__)

@home.route('/api/cadastrar', methods=['POST'])
def cadastrar():

    response = usuario_obj.cadastrar(request.form)

    return retornoAPI(200, 'success', '')


def retornoAPI(status_code, status, dados):
    return {
        'status_code': status_code,
        'status': status,
        'data': dados
    }