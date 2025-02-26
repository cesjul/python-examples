import json

class Carro:
    def __init__(self, nome):
        self._nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def nome_carro(self):
        return self._nome
    
    @nome_carro.setter
    def nome_carro(self, carro):
        self._nome = carro

    @property
    def motor_do_carro(self):
        return self._motor

    @motor_do_carro.setter
    def motor_do_carro(self, motor):
        self._motor = motor.nome_motor
        motor.carros_equipados(self._nome)

    @property
    def fabricante(self):
        return self._fabricante    
    
    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante.nome_fabricante
        fabricante.carros_produzidos(self._nome)
        return f'{self._nome} é fabricado por {fabricante.nome_fabricante}'

class Motor:
    def __init__(self, nome):
        self._nome = nome
        self._lista_carros = []
        self._fabricante = None
    
    @property
    def nome_motor(self):
        return self._nome
    
    @nome_motor.setter
    def nome_motor(self, motor):
        self._nome = motor

    def carros_equipados(self, carro: Carro):
        self._lista_carros.append(carro)

    def listar_carros(self):
        return f'{self._nome} é usado em:{(self._lista_carros)}'
    
    @property
    def fabricante(self):
        return self._fabricante    
    
    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante.nome_fabricante
        fabricante.motores_produzidos(self._nome)
        fabricante.relacao_motores_carros(self._nome, self._lista_carros)
        return f'{self._nome} é fabricado por {fabricante.nome_fabricante}'

class Fabricante:
    def __init__(self, nome):
        self._nome = nome
        self._lista_carros = []
        self._lista_motores = []
        self._dict_motor_carro = {}

    @property
    def nome_fabricante(self):
        return self._nome
    
    @nome_fabricante.setter
    def nome_fabricante(self, valor):
        self._nome = valor
 
    def carros_produzidos(self, carro: Carro):
        self._lista_carros.append(carro)
        
    def listar_carros(self):
        return f'{self._lista_carros} são os modelos produzidos por {self._nome}'
    
    def motores_produzidos(self, motor: Motor):
        self._lista_motores.append(motor)
    
    def listar_motores(self):
        return f'{self._lista_motores} são os modelos produzidos por {self._nome}'

    def relacao_motores_carros(self, motor, lista):
        self._dict_motor_carro.update({

                motor: lista

        })

    def exibir_relacao(self):
        return self._dict_motor_carro
    
 ######################################################################################################################################   


f1 = Fabricante('Nissan')
c1 = Carro('Sentra')
m1 = Motor('MR20')
c2 = Carro('Tiida')
c3 = Carro('Livina')
c2.motor_do_carro = m1
c3.motor_do_carro = m1
m2 = Motor('MR18')
m3 = Motor('MR36')
m1.fabricante = f1
m2.fabricante = f1
m3.fabricante = f1
c1.fabricante = f1
c2.fabricante = f1
c3.fabricante = f1
print(f1.listar_motores())
print(f1.listar_carros())

print(m1.listar_carros())
print(c2.motor_do_carro)
print(f1.exibir_relacao())

f2 = Fabricante('Honda')
c2_1 = Carro('Civic')
c2_2 = Carro('Fit')
m2_1 = Motor('iVTEC')
m2_2 = Motor('Earth Dreams')

c2_1.fabricante = f2
c2_2.fabricante = f2
m2_2.fabricante = f2
m2_1.fabricante = f2
c2_1.motor_do_carro = m2_1
c2_2.motor_do_carro = m2_2

dados = (f1.__dict__, f2.__dict__)

with open('aula84_2.json', 'w', encoding= 'utf-8') as arquivo:
    json.dump(dados, arquivo, indent=2, ensure_ascii= False)