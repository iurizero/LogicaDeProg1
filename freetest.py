lista =[1, 2, 5, 6, 77, 2, 13, 55]

lista.sort()
print(lista)
lista.reverse()
print(lista)


print(f"{sum(lista)}")

# Cria uma lista com 5 números
numeros = [10, 20, 30, 40, 50]

# Exibe a lista formatada sem colchetes
print(f"Números: {', '.join(map(str, numeros))}") 


dicionario_teste = {}

dicionario_teste.update({'Preferencial': 'Ana'})
dicionario_teste.update({'Comum': 'Bruno'})
print(dicionario_teste)
