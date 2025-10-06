a = 1
lista = []
while a != 0:
    a = int(input("\nDigite um valor pra ser agregado na lista (O NUMERO ZERO ENCERRA O PROGRAMA): "))
    lista.append(a)

print(f"\nOs números digitados foram {lista}")

somalista = sum(lista)
medialista = sum(lista) / len(lista)

print(f"\nA soma dos números da lista é {somalista}")
print(f"\nA média dos números da lista é de {medialista}")