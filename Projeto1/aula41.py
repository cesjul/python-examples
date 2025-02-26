#round e imprecisao com numeros de ponto flutuante
import decimal as dec


numero1 = dec.Decimal('0.1')
numero2 = dec.Decimal('0.7')
numero3 = numero1 + numero2
print(numero3)
print(round(numero3, 5))