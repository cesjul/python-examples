import os, json

NOME_ARQUIVO = 'aula114.json'
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 
                  NOME_ARQUIVO           )

) 

filme = {'title': 'O Senhor dos Anéis: A Sociedade do Anel', 
        'original_title': 'The Lord of the Rings: The Fellowship of the Ring',
        'is_movie': True,
        'imdb_rating': 8.8, 
        'year': 2001, 
        'characters': ['Frodo', 
                        'Sam',
                    'Gandalf',
                    'Legolas', 
                    'Boromir'
        ], 
        'budget': None}

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
    json.dump(filme, arquivo, indent=2, ensure_ascii= False)

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r')as arquivo:
    filme_recebido = json.load(arquivo)
    print(filme_recebido)