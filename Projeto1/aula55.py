#lambda e sort/sorted

lista = [
        {'nome': 'A', 'sobrenome': 'D'},
        {'nome': 'B', 'sobrenome': 'C'},
        {'nome': 'C', 'sobrenome': 'B'},
        {'nome': 'D', 'sobrenome': 'A'},
]

def exibe(lista):
    for item in lista:
        print(item)
    print()



lista1 = sorted(lista, key = lambda item: item['nome'])
lista2 = sorted(lista, key = lambda item: item['sobrenome'])


exibe(lista1)
exibe(lista2)

def exibe_argumentos_nomeados(**kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)

exibe_argumentos_nomeados(**lista[0])