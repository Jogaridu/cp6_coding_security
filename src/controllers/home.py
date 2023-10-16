from flask import Blueprint
import sys
import os
import datetime
import locale

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'models'))
from cliente import cliente_obj

home = Blueprint('home', __name__)

@home.route('/api/monitorar')
def api_monitorar():

    locale.setlocale(locale.LC_TIME, 'pt_BR')
    data_atual = datetime.datetime.now()

    dia_atual = data_atual.strftime('%d')
    mes_atual = data_atual.strftime('%B').capitalize()
    
    data = {'status': 'sucesso'}

    return retornoAPI(200, 'success', {dia_atual: dia_atual})


def retornoAPI(status_code, status, dados):
    return {
        'status_code': status_code,
        'status': status,
        'data': dados
    }