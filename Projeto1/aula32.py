frase = 'O Python é uma linguagem de programacão'\
        ' multiparadigma.'\
        'O Python foi criado por Guido van Rossum'

i = 0
vezes_apareceu = 0
letra_mais_repetida = ''



while i < len(frase):
    letra_atual = frase[i]


    if letra_atual == ' ':
        i += 1
        continue


    quantas_vezes_apareceu = frase.count(letra_atual)


    if vezes_apareceu < quantas_vezes_apareceu:
        vezes_apareceu = quantas_vezes_apareceu
        letra_mais_repetida = letra_atual
    
    i += 1

print(f'A letra mais repetida foi "{letra_mais_repetida}",'
      f'aparecendo {vezes_apareceu}x')
   