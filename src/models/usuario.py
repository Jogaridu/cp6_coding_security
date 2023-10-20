import os
import sys
import bcrypt
import jwt
import datetime
from decouple import config


sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'database'))
from conexao_db  import instanciar_usuarios

SECRET_KEY = config('SECRET_KEY')

# Instância do banco
colecao_usuario = instanciar_usuarios()


class Usuario:

    jwt = ''
 
    def cadastrar(self, body):
        
        dados = {
            'email': body['email'],
            'nome': body['nome'],
            'usuario': body['usuario'],
            'senha': bcrypt.hashpw(body['senha'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
        }

        existe = colecao_usuario.find_one({ 'usuario': body['usuario'] })

        if existe == None:
            colecao_usuario.insert_one(dados)
            token = self.auth(body['usuario'])
            return token
        
        return False


    def login(self, usuario, senha):
        
        usuario = colecao_usuario.find_one({ 'usuario': usuario })

        if usuario == None:
            return False


        if bcrypt.checkpw(senha.encode('utf-8'), usuario['senha'].encode('utf-8')):
            token = self.auth(usuario['usuario'])
            return token
        else:
            return False

    def auth(self, usuario):
        
        payload = {
            "sub": usuario,  # Assunto
            "name": "Usuário autenticado",
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)  # Tempo de expiração (24 hora a partir de agora)
        }

        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        self.jwt = token
        
        return token

       
usuario_obj = Usuario()
