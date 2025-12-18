frase = str(input("Digite a frase a ser verificada: ")).lower()

contador = {}

for i in frase:
    if i.isalpha():
        if i in contador:
            contador[i] += 1
        else:
            contador[i] = 1

print("Quantidade de cada letra: ")
for i, qtd in contador.items():
    print(f"{i} => {qtd}")
