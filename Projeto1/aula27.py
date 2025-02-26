#Estrutura de repeticao
# While, executa um bloco de codigo enquanto a condicao for verdadeira

# condicao = input('entrar ou sair? ')

# while condicao == 'entrar':
#     nome = input('Digite seu nome: ')

#     if nome == 'sair':
#         break

# print('acabou')

contagem = 0
entrada = input('V ou P: ')


while True:
    
    if entrada == 'V' and contagem < 100:
        contagem += 1
        if contagem == 45:
            continue 
    
    print(contagem)

   

    if entrada == 'P' or contagem == 100:
        break
