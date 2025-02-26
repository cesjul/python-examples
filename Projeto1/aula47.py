# empacotamento de argumentos nao nomeados

def multi(*args):
    total = 1
    for num in args:
        total *= num
    print(total)
    return total

multi(60, 60)

def par_impar(x):

    par_ou_impar = ''
    resto_por_2 = x % 2

    if resto_por_2 == 0:
        par_ou_impar = 'Par'
    else:
        par_ou_impar = 'Impar'
    
    return par_ou_impar

print(par_impar(6757))