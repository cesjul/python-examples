# formatando strings usando o format 

a = 'A'
b = 'B'
c = 1.2

d = 3.141751
e = 'esse é o pi'

formatacao = 'a = {0} b ={1} c= {nome:.2f}'
formato = formatacao.format(
    a, b, nome = c

)

print(formato)

print(f'{e}:{d:.2f}')