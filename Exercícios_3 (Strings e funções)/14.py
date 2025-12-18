palavra = input("Digite a palavra: ")
largura = int(input("Digite a largura desejada: "))
alinhamento = input("Escolha o alinhamento (E - esquerda, C - centro, D - direita): ").upper()

if len(palavra) >= largura:
    print(palavra)
else:
    espacos = largura - len(palavra)

    if alinhamento == "E":
        resultado = palavra + " " * espacos
    elif alinhamento == "D":
        resultado = " " * espacos + palavra
    elif alinhamento == "C":
        esquerda = espacos // 2
        direita = espacos - esquerda
        resultado = " " * esquerda + palavra + " " * direita
    else:
        resultado = palavra

    print(resultado)
