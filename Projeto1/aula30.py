#Exercicio com while

nome = input('Digite seu nome: ')
caracter = input('Digite o caracter: ')
tamanho_nome = len(nome)
indice = 0
novo_nome = ''




while indice < tamanho_nome:
   
   letra = nome[indice]
   novo_nome += caracter + letra
   indice += 1
   

   if indice == tamanho_nome:
     print(novo_nome)


  





   
