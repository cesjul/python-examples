#list

nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')

lista = [nome, sobrenome, 10, 30]
lista1 = [1, 2, 3 ,4]
lista.insert(-1, 'nome')
lista2 = lista + lista1
lista3 = lista1.extend(lista2)
lista4 = lista1.copy()

print(lista)
print(lista2)
print(lista3)
