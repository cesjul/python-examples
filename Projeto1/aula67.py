#variavel livre e nonlocal

# def externa():
#     a = 0
#     def interna():
#         return a
#     return interna

def concatenar(primeiro_valor):
    primeira_parte = primeiro_valor
    def interna_conc(segunda_parte):
        nonlocal primeira_parte # variavel livre, local da primeira funcao, nonlocal a torna nao local
        primeira_parte += segunda_parte
        return primeira_parte
    return interna_conc

p1 = concatenar('oi')
p2 = p1(' burro')
print(p2)