#exercicio

lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]


k = 0

def verifica_duplicata(lista):
    j = 0
    numero_total = ''
    menor_distancia_segunda_ocorrencia = 10
    verificou_repeticao = None
    mais_repetido = 0

    while j <= 9:
        aparaceu = 0
        repetiu = 0
        primeira_ocorrencia = 0
        segundo_ocorrencia = 0
        mais_repetido = 0

        for i, numero in enumerate(lista, start = 1):
            numero_total += str(numero)
        
            if numero_total[j] == str(numero):
                aparaceu += 1

                if aparaceu == 1:
                    primeira_ocorrencia = i
                if aparaceu == 2:
                    segundo_ocorrencia = i

            

                
                
        menor_distancia_segunda_ocorrencia_atual = segundo_ocorrencia - primeira_ocorrencia

        if menor_distancia_segunda_ocorrencia >= menor_distancia_segunda_ocorrencia_atual and menor_distancia_segunda_ocorrencia_atual > 0:
            menor_distancia_segunda_ocorrencia = menor_distancia_segunda_ocorrencia_atual
            verificou_repeticao = 1
            
            
            


        repetiu += aparaceu - 1
        
        if mais_repetido < repetiu:
            mais_repetido = repetiu
        
        


        if i == 10:
            j += 1        
    
        if repetiu > 0 and verificou_repeticao is not None:
            return 3
    
    if mais_repetido == 0:
        return -1


for lista in lista_de_listas_de_inteiros:
    print(lista)
    k += 1

   
verifica_duplicata(lista_de_listas_de_inteiros[1])
print(verifica_duplicata(lista_de_listas_de_inteiros[1]))

#outra solucao

# def encontra_primeiro_duplicado(lista_de_inteiros):
#     numeros_checados = set()
#     primeiro_duplicado = -1

#     for numero in lista_de_inteiros:
#         if numero in numeros_checados:
#             primeiro_duplicado = numero
#             break

#         numeros_checados.add(numero)

#     return primeiro_duplicado


# for lista in lista_de_listas_de_inteiros:
#     print(
#         lista,
#         encontra_primeiro_duplicado(lista)
#     )