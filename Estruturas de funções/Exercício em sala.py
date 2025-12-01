def primo(n):
    if n < 2:
        return False
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    for i in range(3, n):
        if n % i == 0:
            return False
    
    return True


N = int(input("Digite um número inteiro positivo N: "))

print(f"Primos entre 1 e {N}:")
for numero in range(1, N + 1):
    if primo(numero):
        print(numero)


