n1 = float(input("Digite um número: "))

while n1 <= 0:
    n1 = float(input("Inválido, digite um número positivo"))
    
quadrado = n1 ** 2
raiz = n1 ** 0.5

print(f"A raiz do número é {raiz} e seu quadrado é {quadrado}")