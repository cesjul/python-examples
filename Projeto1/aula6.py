#Variaveis, devem comecar com letra minuscula e pode conter numeros e underline
idade = 20
maior_de_idade = idade >= 18
nome = 'Julio'
sobrenome = 'Cesar'
dia_nascimento = '7' + '/'
mes_nascimento = '7' + '/'
ano_nascimento = '2003'
data_nascimento = (dia_nascimento + mes_nascimento + ano_nascimento)
#No exercicio o correto seria ano_nascimento = 2024 - idade
altura_metros = 1.8
sexo = ('masculino', 'feminino')
sexo_correspondente = sexo[0]
#--------------------------------------------------------------------------------

print('Nome:',nome)
print('Idade:', idade)

if(maior_de_idade == False):
    print(nome, 'não é maior de idade')
else:
    print(nome, 'é maior de idade')


print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', data_nascimento)
print('Altura em metros:', altura_metros)
print('Sexo:', sexo_correspondente)

if(sexo_correspondente == 'masculino'):
    print('Bem-vindo senhor', nome,'é otimo te-lo conosco.')
else:
    print('Bem-vinda Senhora', nome,'é ótimo te-la conosco.')