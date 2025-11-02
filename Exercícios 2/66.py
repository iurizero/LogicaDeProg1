lista = []

for i in range(10):
    a = int(input(f"Digite o {i+1} núemero a ser adicionado: "))
    lista.append(a)

maior = max(lista)
posi = lista.index(maior)

print(f"O maior número digitado foi: {maior} e sua posição na lista era {posi}")
