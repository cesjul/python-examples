lista_cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_uf = ['BA', 'SP', 'MG', 'RJ']
nova_lista = []

# def decorator(func):
#    def inner(*args, **kwargs):
#        a, b = args
#        for i, value in enumerate(a):
#            setted_tuple =(a[i], b[i])
#            nova_lista.append(setted_tuple)
#        return nova_lista      
#    return inner
            


# def gether_tuple_into_list(a, b):
#     setted_tuple = (a, b)
#     nova_lista.append(setted_tuple)
#     return nova_lista


# @decorator
# def executa_funcao(a, b):
#     return nova_lista



# dec = executa_funcao(lista_cidades, lista_uf)
# print(dec)
dicionario = []

def zipper(lista1, lista2):
    lista_menor = []

    if len(lista1) > len(lista2):
        lista_menor = lista2
    elif len(lista1) == len(lista2):
        lista_menor = lista1
    else:
        lista_menor = lista1

    for i, cidade in enumerate(lista_menor):
        tupla = (lista_cidades[i], lista_uf[i])
        nova_lista.append(tupla)
    return nova_lista

print(zipper(lista_uf, lista_cidades))

dicionario = [
    {'Cidade:': valor} if i == 0 else {'UF:': valor}
    for item in nova_lista
    for i, valor in enumerate(item)
]

def zipper_dicionario(*args):
    dict1 = {}
    for i, item in enumerate(args, start=1):
        if i%2 != 1:

            dict1.update({
                item[i-1] : item[i],

            })

    print(dict1)

zipper_dicionario(dicionario)
print(dicionario)

print(10%2)
# {'Cidade:': valor} if i == 0 else {'UF:': valor}