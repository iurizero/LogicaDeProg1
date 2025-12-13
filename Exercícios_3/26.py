def media_de_lista(lista):
    return sum(lista)/len(lista)

a = []

for i in range (5):
    a.append(float(input(f"Digite o {i+1} valor a ser adicionado a lista: ")))
print(a)   
print(f"A média dos valores inseridos foi de {media_de_lista(a)}!")