# def, cria funcoes

def funcao_soma(a, b, c = None):

    if c is not None:
        soma = a + b + c
    else:
        soma = a + b
    
    print(soma)
    return soma
    
funcao_soma(10, 30, 1)

