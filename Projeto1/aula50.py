# def cria_multi_divi(valor):
#     def multi_divi(fator):
#         multiplicar = valor*fator
#         dividir = valor/fator
#         return [multiplicar, dividir]
#     return multi_divi

# multi_divi_5 = cria_multi_divi(5)
# multi_divi_90 = cria_multi_divi(90)


# print(multi_divi_5(5))
# print(multi_divi_90(7))
        
def cria_formatacao(texto):
    def formatacao(caracter):
        palavra = ''
        for letra in texto:
            palavra += letra + caracter
        return palavra
    return formatacao

formata_texto = cria_formatacao('gol do havai contra o bahia e o juiz deu até uma pirueta')
print(formata_texto('/'))


