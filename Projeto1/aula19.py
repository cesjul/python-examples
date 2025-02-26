#Formatacao strings com f-strings
#> - Esquerda, < - Direita

variavel = 'cvb'

print(f'{variavel:-^11}')
print(f'{variavel:->11}')
print(f'{variavel:-<11}')

print(f'{23144341.5768:,.2f}')
print(f'O hexadecimal de 1500 é{1500: 08x}') #convertendo decimal para hexadecimal com f-strings