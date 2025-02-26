import json

CAMINHO_ARQUIVO = 'aula79a.json'


""" 
Este modulo cria objetos do tipo Carro para serem importados a outro modulo


"""


class Carro:
    def __init__(self, marca, modelo, ano, versao, transmissao):
        self._modelo = modelo
        self._marca = marca
        self._ano = ano 
        self._versao = versao
        self._transmissao = transmissao

    @property
    def modelo(self):
        return self._modelo
    
    @modelo.setter
    def modelo(self, valor):
        self._modelo = valor

    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, valor):
        self._marca = valor
    
    @property
    def ano(self):
        return self._ano
    
    @ano.setter
    def ano(self, valor):
        self._ano = valor
    
    @property
    def versao(self):
        return self._versao
    
    @versao.setter
    def versao(self, valor):
        self._versao = valor
    
    @property
    def transmissao(self):
        return self._transmissao
    
    @transmissao.setter
    def transmissao(self, valor):
        self._transmissao = valor
        
    """
    Essa classe cria objetos do tipo Carro, tendo como atributos modelo, marca, ano, versao e transmissao
    """

def update_value(self, attribute):
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
        json.dump(self.__dict__[attribute], arquivo, indent=2, ensure_ascii= False)

carro = { 'Marca': 'Toyota',
          'Modelo': 'Corolla',
          'Ano': '2013',
          'Versão': 'XEI',
          'Transmissão': 'AT'
}


corolla = Carro(*list(carro.values()))


def dump_json():
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
        json.dump(corolla.__dict__, arquivo, indent=2, ensure_ascii= False)

if __name__ == '__main__':
    dump_json()

