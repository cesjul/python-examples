#exercicio
import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
print(*produtos, sep='\n')
print()
novo_produtos = copy.deepcopy(produtos)

novo_produtos = [
                {**dicionario, 'preco': round(dicionario['preco'] * 1.1, 2)}
                
                for dicionario in produtos
                
]

print(*novo_produtos, sep='\n')
print()

produtos_ordenados_por_nome = copy.deepcopy(produtos)
produtos_ordenados_por_nome.sort(key = lambda item: item['nome'], reverse=True)

print(*produtos_ordenados_por_nome, sep='\n')

produtos_ordenados_por_preco = copy.deepcopy(produtos)
produtos_ordenados_por_preco.sort(key = lambda item: item['preco'])
# print(*produtos_ordenados_por_preco, sep='\n')