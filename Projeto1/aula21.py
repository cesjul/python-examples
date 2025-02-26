# try/except

numero_str = input('Digite um numero: ')

try:
    print(numero_str.isdigit())
    numero_int = int(numero_str)
    print(f'o dobro de {numero_str} é {numero_int * 2}')

except:
    print('Isso náo é um numero')