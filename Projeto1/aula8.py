#Concatenando str e utilizando operadores artiméticos

concatenacao = 'A' + 'B' + 'C'
print(concatenacao)


a_dez_vezes = 10 * 'A'
julio_tres_vezes = 3 * 'julio'

print(a_dez_vezes)
print(julio_tres_vezes)

#Precedencia, é a ordem com que seram executadas cada operacao
'''
1. ()
2. **
3. * / // %
4. + -
'''

conta = (3*6) - (5*2)
print(conta)


if(conta >= 7):
    print('Conta maior que oito')
else:
    conta = conta
