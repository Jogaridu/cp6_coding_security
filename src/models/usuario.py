import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'database'))
from conexao_db  import instanciar_usuarios


# Instância do banco
colecao_usuario = instanciar_usuarios()


class Usuario:

    # UUID
    id = ''

    def __init__(self):
        self.id = '123'

 
    def cadastrar(self, body):
        
        dados = {
            'email': body['email'],
            'nome': body['nome'],
            'usuario': body['usuario'],
            'senha': body['senha'],
        }

        response = colecao_usuario.insert_one(dados)
        print(response)
        self.auth(body['usuario'], body['senha'])

        return 

    def auth(self, usuario, senha):
        print(usuario, senha)
        print('logou com sucesso')

      
       
usuario_obj = Usuario()
