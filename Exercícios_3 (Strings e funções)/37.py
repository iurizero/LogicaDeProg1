def imprime_retangulo(largura, altura, caractere):
    for i in range(altura):
        for j in range(largura):
            print(caractere, end='')
        print()



imprime_retangulo(10, 5, "*")