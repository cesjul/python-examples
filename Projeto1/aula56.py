# list comprenhension
import random
aumento = ''


lista = [
         
        numero
        for numero in range(10)

]

# print(lista)

moedas = [
                {'moeda': 'dolar', 'cotacao': 5.6},
                {'moeda': 'euro', 'cotacao': 5.8},
                {'moeda': 'libra', 'cotacao': 6.0},
                {'moeda': 'peso', 'cotacao': 0.9},
                {'moeda': 'rubro', 'cotacao': 1.0},
        ]

for i in range(5):
        aumento += str(random.randint(0,9))

aumento_float = float('1.0' + aumento)

nova_lista = [
    {**dicionario, 'cotacao': dicionario['cotacao'] * aumento_float, 'equivalente em reais': 1 / dicionario['cotacao'] * aumento_float}
    for dicionario in moedas
    if dicionario['cotacao'] < 6.0
]

print(*nova_lista, sep= '\n')



for moeda in nova_lista:
    exibi_moeda = ''

    for valor in moeda:
        # print(valor, moeda[valor])
        exibi_moeda += valor + ' : ' + str(moeda[valor]) + ' | '

    print(exibi_moeda)
    print()    