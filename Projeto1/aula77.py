#programacao orientada a objetos
import json

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
     
        self.sobrenome = sobrenome
        
    
    def nome_maisculo(self):
        return str(self.nome).title()
    
    def sobrenome_maisculo(self):
        return str(self.sobrenome).title()
   
    def quant_letras(self):
        return len(self.nome) + \
               len(self.sobrenome)

    def tamanho_nome(self):
        esse_nome_é = ''
        valor = len(self.nome)
        if len(self.nome) < 4:
            esse_nome_é = 'pequeno'
        elif len(self.nome) == 4 or len(self.nome) < 7:
            esse_nome_é = 'médio'
        elif len(self.nome) >= 7:
            esse_nome_é = 'grande'

        return esse_nome_é



CAMINHO_DADOS_INSTANCIA = 'aula77_a.json'
CAMINHO_CLASSE = 'aula77_b.txt'

pessoa1 = Pessoa('nome', 'sborenome')
pessoa2 = Pessoa('nome1', 'sobrenome1')
numero = Pessoa(1, 2)

dados_pessoa = [pessoa1.__dict__, pessoa2.__dict__, numero.__dict__] 



    

with open(CAMINHO_DADOS_INSTANCIA, 'w', encoding= 'utf-8') as arquivo:
    json.dump(dados_pessoa, arquivo, indent=2, ensure_ascii= False)