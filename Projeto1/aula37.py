lista1 = ['Nome', 'Nome1', 'Nome2', 0, 1, 2, 3, 4, 5, 6]

i = 0
_, _, nome, *_ = ['Nome', 'Nome1', 'Nome2', 0, 1, 2, 3, 4, 5, 6]
for nome in lista1: # for não funciona bem com desempacotamento
    print(i, nome)
    i += 1

print(nome)