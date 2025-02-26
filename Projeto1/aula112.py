import os, shutil

HOME = os.path.expanduser('~')
IMAGENS = os.path.join(HOME, 'OneDrive', 'Documentos', 'Projetos')
NOVO_CAMINHO = os.path.join(HOME, 'OneDrive','Documentos', 'Projetos-copia')
NOVA_PASTA = os.makedirs(NOVO_CAMINHO, exist_ok= True)

# for root, dirs, files in os.walk(IMAGENS):
    
    
#     for dir in dirs:
#         novos_diretorios = os.path.join(NOVO_CAMINHO, dir)
#         os.makedirs(novos_diretorios, exist_ok=True)
#         print(os.path.join(IMAGENS, dir))
#         shutil.copy(os.path.join(IMAGENS, dir), novos_diretorios)
#         print('   ', dir)

for root, dirs, files in os.walk(IMAGENS):
    for dir_ in dirs:
        caminnho_novo_diretorio = os.path.join(
            root.replace(IMAGENS, NOVO_CAMINHO), dir_
        )
        os.makedirs(caminnho_novo_diretorio, exist_ok=True)

    for file in files:
        caminho_arquivo = os.path.join(root, file)
        caminnho_novo_arquivo = os.path.join(
            root.replace(IMAGENS, NOVO_CAMINHO), file
        )
        shutil.copy(caminho_arquivo, caminnho_novo_arquivo)