'''
None é o nao valor
is e is not checam o id do objeto, bem como o tipo ou valor

'''
condicao = False
passou_no_if = None
variavel = 1




if condicao:
    print('Algo aconteceu')
    passou_no_if = True
else:
    print('Nada aconteceu')

print(passou_no_if , passou_no_if is None)
print(passou_no_if , passou_no_if is not None)

if type(variavel) is int:
    print(f'Variavel é {type(variavel)}')
        