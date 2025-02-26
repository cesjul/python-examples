# funcao range

numeros = range(10)


for numero in numeros:
    print(numero)

# funcionamento do for

texto = 'Exemplo'
iterador = iter(texto)

while True:
    try:
        letra = next(iterador) # letra pode qualquer outra variavel, como esta no for acima
        print(letra)
    except StopIteration:
        break

# Sendo assim no for a variavel a ser iterada será tratada como next(iter(variavel)) 
# a variavel criada para o for será variavel_for = next(iter(variavel)