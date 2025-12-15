frase = str(input("Digite a frase: ")).lower()

lista = []

for i in set(frase):
    if i.isalpha():
        x = frase.count(i)
        lista.append(f"{i} = {x}")
    
print(lista)