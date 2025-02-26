# Exercicio palavra secreta



print('Existe uma palavra secreta')
palavra = 'rapadura'
tentativas = 0
letra_digitada = ''
i = None

while True:
    

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Digite apenas uma letra')
        continue

    if letra in palavra:
        letra_digitada += letra
        tentativas += 1
    else:
        tentativas += 1
    

    palavra_formada = ''

    for letra_secreta in palavra:
        if letra_secreta in letra_digitada:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '_'
    
    print(palavra_formada)

    if palavra_formada == palavra:
        print(f'Voce descobriu a palavra secreta'
              f' "{palavra}" com {tentativas} tentativas')
        break

    
  

    