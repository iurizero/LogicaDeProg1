def fatorial(a):
    total = 1
    for i in range (1, a+1):
        total *= i
        
    return total

numero = int(input("Digite o número pra ver seu fatorial: "))

print(f"O fatorial de {numero} é igual a {fatorial(numero)}!")