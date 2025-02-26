# Fatiamento de strings

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')



# print(variavel[4:]) # Irá exibir do indice 4 até o final
# print(variavel[4:8:2]) # Irá exibir do indice 4 até o 8, com o passo que esta pulando de dois em dois nesse caso
# print(variavel[:8]) # Irá exibir do indice 8 para trás
# print(len(variavel)) # Funcao len() retorna o numero de caracteres 
# print(variavel[::-1]) # Passo negativo, inverte a string

if nome != '' and idade != '':
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome contem espacos')
    else:
        print('Seu nome nao contem espacos')
    print(f'Seu nome possui {len(nome)} letras')
    print(f'A primeira letra do seu nome é: {nome[:1]}')
    print(f'A ultima letra do seu nome é:{nome[:len(nome) -2: -1]} ')
else:
    print('Nenhum dos campos podem ficar vazios')


