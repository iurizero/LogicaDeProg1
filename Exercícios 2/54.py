n1 = int(input("Digite o número a ser comparado: "))
impares = 1
lista = [1]

while impares < n1:
    impares += 2
    lista.append(impares)
    
print(lista)