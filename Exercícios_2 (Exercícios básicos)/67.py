lista = []
lista_inversa = []

for i in range(6):
    a = int(input(f"Digite o {i+1} número a ser inserido: "))
    lista.append(a)

for a in range(6, 0, -1):
    b = lista[a-1]
    lista_inversa.append(b)

print(lista_inversa)