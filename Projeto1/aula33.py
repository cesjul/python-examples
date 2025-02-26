# Estrtura de repeticao: for

string = 'Declaro que entreguei todos os documentos exigidos para efetivação da matrícula, conforme'\
'minha aprovação no Processo Seletivo – Concurso Vestibular deste semestre letivo – Vestibular 2 º'\
'semestre de 2024, e, sob as penas da Lei, informo que todas as informações e documentos'\
'prestados são verdadeiros, para tanto anexo uma cópia ou declaração dos seguintes documentos e'

i = 0
vezes_apareceu = 0
letra_mais_repetida = ''


for letra in string:
    letra_atual = string[i]

    if letra_atual == ' ':
        i += 1
        continue
    
    quantas_vezes_repetiu = string.count(letra_atual)

    if vezes_apareceu < quantas_vezes_repetiu:
        vezes_apareceu = quantas_vezes_repetiu
        letra_mais_repetida = letra_atual
    
    i += 1


print(letra_mais_repetida, vezes_apareceu)
    