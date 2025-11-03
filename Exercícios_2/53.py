contador = 1
lista_numeros = []
n1 = 0

while contador <= 10:
    n1 = int(input(f"Digite o {contador} número a ser adicionado: "))
    lista_numeros.append(n1)
    contador += 1
    
lista_numeros.sort()

menor = lista_numeros[-1]
maior = lista_numeros[0]

print(f"Maior número é {maior}")
print(f"Menor número é {menor}")