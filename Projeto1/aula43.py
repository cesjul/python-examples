# listas dentros de listas

escola = [ ['Oi', 'Albverto', 'Givaldo'],
          
           ['Bauduco', 'Tigrinho'], 

           ['nome', 'nome1', 'nome2']       
]

# oitavo_ano = escola[0]
# setimo_ano = escola[1]
# sexto_ano = escola[2]
# i = 8
# print(oitavo_ano)

# for sala in escola:
#     print(f'{i} ano')
#     i -= 1
#     for aluno in sala:
#         print(aluno)

print(*escola, sep ='\n')