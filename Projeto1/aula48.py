#Closure e funcoes que retornam funcoes

def nome_sobrenome(sobrenome):
    def definir_nome(nome):
        return f'Seu nome é {nome} {sobrenome}'
    return definir_nome

sobrenome_1 = nome_sobrenome('SOBRENOME')
print(sobrenome_1('NOME1'))
print(sobrenome_1('NOME2'))
   

        