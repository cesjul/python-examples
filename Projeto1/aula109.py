import os

caminho = os.path.join('C:\\Users', 'user', 'directory', 'documents',\
                                                      'file')
print(caminho)

for pasta in os.listdir(caminho):
    print(pasta)
    cmainho_completo = os.path.join(caminho, pasta)
    for arquivo in os.listdir(cmainho_completo):
        print('  ', arquivo)