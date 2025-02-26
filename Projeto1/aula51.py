# dicionarios

pessoa = {'nome': 'Nome da pessoa',
          'sobrenome': 'Sobrenome da pessoa',
          'idade': 'Idade da pessoa',
          'altura': 'Altura da pessoa',
          'enderecos':[
            {'rua': 'rua da pessoa', 'numero': 'numero da casa'},
            {'rua': 'outra rua da pessoa', 'numero': 'outro numero da casa'}
            ] 
          }

print(pessoa['enderecos'][0]['rua'])

chave = 'nome'


chave_nao_achada = pessoa.get('nome', 17)

if chave_nao_achada == 17:
    print('chave nao achada')


palavra = ['basquete']

if True:
    palavra_editada = palavra[0].replace('a', 'o')
    print(palavra_editada)

pessoa.pop('enderecos'[0][0])
print(pessoa)