# split, join

texto = '  Ola mundo cruel  '
texto_cru = texto.split('o')

lista_stripada = []

for i, texto in enumerate(texto_cru):
    lista_stripada.append(texto_cru[i].strip())

print(lista_stripada)
print('o '.join(lista_stripada))