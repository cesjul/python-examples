entrada = input('Digite seu nome: ')
nome_valido = entrada.isalpha()


if nome_valido:
    
    if len(entrada) < 2:
        print('Seu nome deve ter mais de uma letra')

    elif len(entrada) <= 4:
        print('Seu nome é curto')

    elif len(entrada) == 5 or len(entrada) == 6:
        print('Seu nome é normal')

    elif len(entrada) > 6:
        print('Seu nome é grande')


else:
    print('Digite apenas letras')