# Para se refirir a uma constante, usar letras maiusculas
# Boas praticas de codigo
# VELOCIDADE = 50


velocidade_lida = 51 # variavel
local_carro = 91

ALCANCE_RADAR = 1
LOCAL_RADAR = 90
VELOCIDADE_PERMITIDA = 50 # constante

velocidade_multavel = VELOCIDADE_PERMITIDA + (VELOCIDADE_PERMITIDA * 0.1)

velocidade_ultrapassada_radar = velocidade_lida > velocidade_multavel

carro_dentro_do_alcance = (LOCAL_RADAR + ALCANCE_RADAR) or \
                          local_carro <= (LOCAL_RADAR - ALCANCE_RADAR)


if velocidade_ultrapassada_radar:
    print('Carro acima do limite')

    if local_carro >= carro_dentro_do_alcance:
        print('Carro multado')
