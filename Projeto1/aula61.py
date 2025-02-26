# funcoes com generator

# def generator(n = 0, max = 10):
#     while True:
#         yield n
#         n += 1

#         if n >= max:
#             return

# def gen2(funcao):
#     yield from funcao()
#     yield 'VOLTEI AQUI'




# g2 = gen2(generator)

# for n in g2:
#     print(n)

def g1():
    yield 1
    yield 2
    yield 3

def g2(funcao):
    yield from funcao()
    yield 7
    yield 8
    yield 9

def g3():
    yield 4
    yield 5
    yield 6

gen = g2(g1)
gen2 = g2(g3)


for n in gen2:
    print(n)


