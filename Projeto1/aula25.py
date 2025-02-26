entrada = input('Que horas são? ')
hora_verificavel = entrada.isdigit() and len(entrada) <= 2 and entrada



if hora_verificavel:

    if entrada >= '0' and entrada <= '11':
        print('Bom dia')
    elif entrada >= '12' and entrada <= '17':
        print('Boa tarde')
    elif entrada >= '18' and entrada <= '23':
        print('Boa noite')
    else:
        print('Digite horas entre 0 e 23')
        
else:
    print('Digite uma hora valida')