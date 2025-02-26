#exercicio

def multiplica_numero(num):
    def duplicar():
        valor = num * 2
        return f'O dobro de {num} é {valor}\n'
    def triplicar():
        valor = num * 3
        return f'O triplo de {num} é {valor}\n'
    def quadruplicar():
        valor = num * 4
        return f'O quadrupulo de {num} é {valor}\n'
    retorno = f'{duplicar()}{triplicar()}{quadruplicar()}'
    return retorno

print(multiplica_numero(69))

# solucao 
# def criar_multiplicador(multiplicador):
#     def multiplicar(numero):
#         return numero * multiplicador
#     return multiplicar


# duplicar = criar_multiplicador(2)
# triplicar = criar_multiplicador(3)
# quadruplicar = criar_multiplicador(4)

# print(duplicar(2))
# print(triplicar(2))
# print(quadruplicar(2))