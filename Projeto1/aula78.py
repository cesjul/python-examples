from aula77 import Pessoa, CAMINHO_DADOS_INSTANCIA
import json

with open(CAMINHO_DADOS_INSTANCIA, 'r') as arquivo:
    dados = json.load(arquivo)
    dicionario = {}
    for i, dado in enumerate(dados):
        pessoa = 'pessoa_' + str(i)
        dicionario.update({

                pessoa : dado

        })

        
    print(dicionario)


    