# usando funcao input()

nome = input('Qual seu nome? ')
altura = input('Qual sua altura? ')
peso = input('Qual seu peso? ')
imc = int(peso)/(float(altura) ** 2)

'''
O mais correto é criar uma nova variavel pra converter 
as variaveis do input para os tipos que seram usados no codigo

peso_int = int(peso)
altura_float = float(altura)
imc = peso_int/(altura_float ** 2)
'''


if imc < 18.5:
    estado = 'Abaixo do normal'

if imc >= 18.5 and imc < 25:
    estado = 'Normal'

if imc >= 25.00 and imc < 29.99:
   estado =  'Acima do normal'

if imc >= 30.00:
    estado = 'Em nível de obesidade'


print(f'{nome} possui IMC de: {imc:.2f}')
print(f'O IMC é considerado {estado}')