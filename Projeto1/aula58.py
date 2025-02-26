# dictionary comprenhansion

dicionario = {
            'chave1': 'valor1',
            'chave2': 'valor2',
            'chave3': 'valor3',

}

novo_dicio = {
            chave: valor + '.'
            
            for chave, valor in dicionario.items()

}

print(novo_dicio)