#manipulacao de arquivos
produtos = [
    'Arroz', 'Feijao', 'Macarrao', 'Tomate', 'Azeite'
]


caminho = 'SEUCAMINHO/PASTA'
caminho += 'Aula74_2.txt'


# arquivo = open(caminho, 'w')

# arquivo.close()
num = 1
num_somado = ''

with open(caminho, 'w') as arquivo:

    # for i in range(10):
    #     num_somado = f'{num} + {num} \r'
    #     num += 1
    #     arquivo.write(num_somado)
    
    for item in produtos:
        item += '\r'
        arquivo.writelines(item)


with open(caminho, 'r') as arquivo:
    arquivo.seek(0,0)
    print(arquivo.read())
    arquivo.seek(0,0)
    print('*' * 15)
    print(arquivo.readline())
    print(arquivo.readlines())