# in e not in
# strings são iteraveis, ou seja, pode-se navegar pelos itens da sting
# sendo assim é possivel passar como argumento cada item da string
# J U L I O
# 0 1 2 3 4

nome = input('Digite um nome: ')
encontrar = input('O que deseja encontrar? ')


if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} nao esta em {nome}')

