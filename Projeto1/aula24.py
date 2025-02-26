numero = input('Digite um numero inteiro: ')
numero_int = None
par_impar = None
resultado_par_impar = None


if numero.isdigit():
    numero_int = int(numero)
    par_impar = numero_int % 2 == 0
    resultado_par_impar = 'impar'

    if par_impar:
        resultado_par_impar = 'par'

    print(f'{numero_int} é {resultado_par_impar}')



else:
    print('Digite um numero inteiro')



