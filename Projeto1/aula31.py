#Calculadora com while

while True:

    valor1 = input('Digite um valor: ')
    valor_num1 = None

    if valor1.replace('.', '').isdigit(): #
        valor_num1 = float(valor1)
    else:
        print('Digite um valor válido')
        break

    valor2 = input('Digite outro valor: ')
    valor_num2 = None

    if valor2.replace('.', '').isdigit():
        valor_num2 = float(valor2)
    else:
        print('Digite um valor válido')
        break

    operacao_str = input('Digite a operacao: ')
    
    resultado = None

    if operacao_str == '+':
        resultado = valor_num1 + valor_num2
    elif operacao_str == '-':
        resultado = valor_num1 - valor_num2
    elif operacao_str == '*':
        resultado = valor_num1 * valor_num2
    elif operacao_str == '/':
        resultado = valor_num1 / valor_num2
    else:
        print('Operacao invalida (apenas: +, -, /, *)')
        break

    print(f'Resultado: {resultado:,.2f}')


    sair = input('Deseja [s]air? ').lower().startswith('s')

    if sair:
        break




