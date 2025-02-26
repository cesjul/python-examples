# latest update in 29/08/2024
# by engeering studant Julio Cesar



def verifica_cpf_repetido(cpf):

    cpf_apenas_numeros_str = ''
    

    for digito in cpf:

        if digito == '.' or digito == '-':
            continue

        cpf_apenas_numeros_str += digito
        

    if cpf_apenas_numeros_str.count(digito) == 11:
        return True
    else:
        return False

def verificando_cpf(cpf):


    cpf_repetido = verifica_cpf_repetido(cpf)
    resultado_soma = 0
    resultado_soma2 = 0
    multiplicador = 10
    multiplicador2 = 11
    cpf_sem_final = cpf[:11]
    digito_final_1_str = ''
    digito_final_2_str = ''
    cpf_completo = ''


    if cpf_repetido:
        return False

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

    cpf_com_final_1 = cpf_sem_final
    
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

    digito_final_2_str = str(digito_final_2)
    cpf_com_final_1 += digito_final_2_str
    cpf_completo = cpf_com_final_1

    if cpf != cpf_completo:
        return False
    else: 
        return True



