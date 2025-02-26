lista1 = [1,2,3,4,5,6,7]
lista2 = [1,2,3,4]

def soma_lista(lista1, lista2):
    lista_menor = []
    lista_maior = []
    lista_soma = []
    if len(lista1) > len(lista2):
        lista_menor = lista2
        lista_maior = lista1
    elif len(lista1) == len(lista2):
        lista_menor = lista1
        lista_maior = lista2
    else:
        lista_menor = lista1
        lista_maior = lista2
    for i, valor in enumerate(lista_menor):
        resultado = lista_menor[i] + lista_maior[i]
        lista_soma.append(resultado)
    return lista_soma

print(soma_lista(lista1, lista2))
