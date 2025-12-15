texto = str(input("Digite a frase desejada: ")).lower()

for i in set(texto):
    print(f"{i} = {texto.count(i)}")