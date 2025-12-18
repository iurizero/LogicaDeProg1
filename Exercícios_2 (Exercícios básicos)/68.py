lista = []
lista_inversa = []

for i in range(6):
    a = int(input(f"Digite o {i+1} valor par a ser checado: "))
    while a%2 != 0:
        a = int(input(f"O {i+1} valor não é par, digite um valor PAR: "))
    lista.append(a)
    
for l in range(6, 0, -1):
    b = lista[l-1]
    lista_inversa.append(b)
    
print(f"A lista de pares invertida é de: {lista_inversa}")