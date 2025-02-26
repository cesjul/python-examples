# Exercicio, calculadora de IMC, IMC = Peso/Altura²

nome = 'Julio'
peso = 75
altura = 1.80
imc = peso/(altura ** 2)


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
print(nome, 'possui IMC igual a:', imc)
print(f'O IMC de {nome} esta {estado}')
