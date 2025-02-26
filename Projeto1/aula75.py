#modulo json

import json

pessoa = {'nome': 'Nome da pessoa',
          'sobrenome': 'Sobrenome da pessoa',
          'idade': 'Idade da pessoa',
          'altura': 'Altura da pessoa',
          'enderecos':[
            {'rua': 'rua da pessoa', 'numero': 'numero da casa'},
            {'rua': 'outra rua da pessoa', 'numero': 'outro numero da casa'}
            ] 
          }



with open('aula75.json', 'w') as arquivo:
    json.dump(
                pessoa,
                arquivo,
                ensure_ascii= False,
                indent= 2
              )