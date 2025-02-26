# exercicio lista de compras
lista_de_compras = []
novo_item = ''
indice_apagar = ''
indice_apagar_int = 0

while True:
    
    acao = input('Deseja inserir, apagar, listar ou sair? ')

    if acao.lower() == 'inserir':
        novo_item = input('Digite o item: ')
        lista_de_compras.append(novo_item)
    
    
    elif acao.lower() == 'apagar':
        indice_apagar = input('Digite o indice a apagar: ')
        


        if lista_de_compras == []:
            print('A lista esta vazia')
            

        if indice_apagar.isdigit() == False:
            print('Digite um valor valido')
            continue
        else:
            indice_apagar_int = int(indice_apagar)


        if len(lista_de_compras) < indice_apagar_int:
            print('Indice invalido')
            continue
        else:
            del lista_de_compras[indice_apagar_int]

    elif acao == 'listar':

        for indice, item in enumerate(lista_de_compras, start= 1) :
            print(indice, item)
        
        if lista_de_compras == []:
            print('A lista esta vazia')

    elif acao == 'sair':
        break

    else:
        print('Digite uma opcao valida')
        
        

        
    
    

    