#Exercicio


j = 1
i = 0
pontuacao = 0


perguntas = [
            {'Pergunta': 'Qual é a capital da França? ',
             'Alternativas': ['São Paulo', 'Lisboa', 'Paris', 'Marselle', 'Londres' ],
             'Respostas': 'Paris'
             },

            {'Pergunta': 'Quanto é a raiz de quadrada de 81? ',
             'Alternativas': ['40,5', '81', '17', '9', '14'],
             'Respostas': '9'
             },

             {'Pergunta': 'Qual o periodo de tempo entre copas do mundo? ',
              'Alternativas': ['4 anos', '2 anos', '3 anos', '5 anos'],
              'Respostas': '4 anos'
             }
]

def verica_resposta():

    resposta = ''
    resposta_valida = resposta_recebida.isdigit() 
    resposta_fora_do_range = int(resposta_valida) > len(alternativas_listadas) \
                               or int(resposta_valida) == 0

    if resposta_valida != True:
        return 1
        
    if resposta_fora_do_range:
        return 1

    resposta_correta = perguntas[i]['Respostas'] == alternativas_listadas[int(resposta_recebida)]

    

    if resposta_correta:
        resposta = 'Resposta Correta \n'
    else:
        resposta = 'Resposta Incorreta \n'

    return resposta



while len(perguntas) >= j:
    alternativas_listadas = {}
    numero_alternativa = None
    alternativas = ''
    pergunta_atual = perguntas[i]['Pergunta'] # Pega as perguntas


        
    for indice, alternativa_atual in enumerate(perguntas[i]['Alternativas'], start=1): # Itera sobre as alternativas 
        alternativas += str(indice) + '. ' + alternativa_atual + ' | '
        alternativas_listadas.update({

            indice: alternativa_atual
        })
    
        
    resposta_atual =  perguntas[i]['Respostas']

    print(pergunta_atual)
    print(alternativas)

    resposta_recebida = input('Digite sua resposta: ')

    
    resposta = verica_resposta()

    if verica_resposta() == 1:
        print('Digite uma resposta valida \n')
        continue
    
    if resposta == 'Resposta Correta \n':
        print(resposta)
        i += 1
        pontuacao += 1
    else:
        print(resposta)
        i += 1

    j += 1

    if j > len(perguntas):

        if pontuacao == 0:
            print(f'Voce nao acertou nenhuma pergunta')
        elif pontuacao > 1:
            print(f'Voce acertou um total de {pontuacao} perguntas')
        else:
            print('Voce acertou 1 pergunta')

        
    

    




