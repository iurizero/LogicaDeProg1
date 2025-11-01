lista = []
lista_quadrado = []

for i in range(10):
    a = int(input(f"Digite o {i+1} valor a ser guardado na lista: "))
    lista.append(a)
    
for l in lista:
    a = l**2
    lista_quadrado.append(a)
    
print(f"A primeira lista foi: {lista}\nA lista ao quadrado é: {lista_quadrado}")