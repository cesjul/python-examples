# formatacao de strings com f
nome = 'Julio'
peso = 75
altura = 1.80
imc = peso/(altura ** 2)
numero = 2 ** 64

if imc < 18.5:
    estado = 'Abaixo do normal!'

if imc >= 18.5 and imc < 25:
    estado = 'Normal'

if imc >= 25.00 and imc < 29.99:
   estado =  'Acima do normal'

if imc >= 30.00:
    estado = 'Obeso'



print(altura, ' m')
print(peso, 'Kg')
print(f'{nome} possui IMC igual a {imc:.2f}') #formatando o numero de casas decimais 
print(f'O IMC de {nome} esta {estado}') # foi formatado com f-string
print(f'{numero:,.2f}')
