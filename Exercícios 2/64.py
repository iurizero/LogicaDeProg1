lista = []
lista_pares = []

for i in range(10):
    a = int(input(f"Digite o {i+1} valor a ser guardado: "))
    lista.append(a)

contador = 0
for l in lista:
    if l%2 == 0:
        contador +=1
        lista_pares.append(l)
print(f"Existem {contador} valores pares na lista!\n Esses são os valores: {lista_pares}")