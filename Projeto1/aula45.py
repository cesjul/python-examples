#gerador de cpf

import random

resultado_soma = 0
resultado_soma2 = 0
multiplicador = 10
multiplicador2 = 11
# cpf_enviado = '454.981.690-27'
# cpf = '454.981.690-27'
cpf_sem_final = ''
digito_final_1_str = ''
digito_final_2_str = ''
cpf_completo = ''

for i in range(9):
    cpf_sem_final += str(random.randint(0, 9))

cpf_com_final_1 = cpf_sem_final
# print(cpf_sem_final)


for digito in cpf_sem_final:

    if digito == '.':
        continue

    digito_int = int(digito)
    resultado = digito_int * multiplicador
    resultado_soma += resultado
    resultado_soma_10 = resultado_soma * 10
    resultado_resto = resultado_soma_10 % 11
    digito_final_1 = resultado_resto
    multiplicador -= 1

if digito_final_1 > 9:
    digito_final_1 = 0
else:
    digito_final_1 = digito_final_1

# print(digito_final_1)
digito_final_1_str = str(digito_final_1)
cpf_com_final_1 += '-' + digito_final_1_str

for digito_2 in cpf_com_final_1:

    if digito_2 == '.' or digito_2 == '-':
        continue

    digito_int2 = int(digito_2)
    resultado2 = digito_int2 * multiplicador2
    resultado_soma2 += resultado2
    resultado_soma_11_2 = resultado_soma2 * 10
    resultado_resto_2 = resultado_soma_11_2 % 11
    digito_final_2 = resultado_resto_2
    multiplicador2 -= 1

if digito_final_2 > 9:
    digito_final_2 = 0
else:
    digito_final_2 = digito_final_2

# print(digito_final_2)
digito_final_2_str = str(digito_final_2)
cpf_com_final_1 += digito_final_2_str
cpf_completo = cpf_com_final_1

j = 0
cpf_formatado = ''
for num in cpf_completo:

    if (j % 3) == 0 and j != 0 and j < 9:
        cpf_formatado += '.' + num
    else:
        cpf_formatado += num
    
    


    j += 1



print(cpf_formatado)





# print('CPF invalido') if cpf_invalido else print('CPF valido')


