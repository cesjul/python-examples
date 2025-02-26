import json
from aula79 import Carro, CAMINHO_ARQUIVO

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    dados = json.load(arquivo)
    

carro = Carro(*list(dados.values()))
carro.transmissao = 'Manual'
dados['_transmissao'] = 'Manual'
print(dados)
with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8')as arquivo:
    json.dump(dados, arquivo, indent=2, ensure_ascii= False)

help(Carro)