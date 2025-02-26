from itertools import product

lista = [

    ['branco', 'preto', 'cinza',],
    ['sedan', 'suv', 'hatch',],
    ['popular', 'medio', 'luxo'],
    ['usado', 'semi-novo', 'zero-km'],
    ['basica', 'intermediaria', 'completa']
]

print(*list(product(*lista)), sep='\n')