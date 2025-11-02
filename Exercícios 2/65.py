lista = []

for i in range (10):
    a = int(input(f"Digite o {i+1} número a ser adicionado: "))
    lista.append(a)
    
menor = min(lista)
maior = max(lista)

print(f"O maior número é {maior} e o menor é {menor}")