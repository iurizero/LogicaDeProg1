def soma_variaveis(lista):
    total = sum(lista)
    return total

quantidade = int(input("Digite a quantidade de variaveis que serão inseridas na soma: "))

lista = []

for i in range (quantidade):
    lista.append(int(input(f"Digite o {i+1} valor a ser inserido: ")))
    
print(f"A soma total dos valores digitados foi de: {soma_variaveis(lista)}")