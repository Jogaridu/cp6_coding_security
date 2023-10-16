import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'database'))
from conexao_db  import instanciar_processos, instanciar_analise


# Instância do banco
colecao_processos = instanciar_processos() # Resultado
colecao_analise = instanciar_analise() # Dados de análise de novo processo


class Cliente:

    # UUID
    id = ''

    def __init__(self):
        self.id = '123'

 
    def iniciar(self):
        print('chamou backend')
      
       
cliente_obj = Cliente()
