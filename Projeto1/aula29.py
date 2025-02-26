# while internos a outros whiles

qtd_linha = 5
qtd_coluna = 5

linha = 1

while linha <= qtd_linha:

    coluna = 1

    while coluna <= qtd_coluna:  # nesse caso, o interpretador ira entrar nesse while e apenas saira quando 
                                 # quando a expressao for falsy, e assim ira executar o que resta no while maior

        print(coluna)
        coluna += 1

    print(linha)
    linha += 1