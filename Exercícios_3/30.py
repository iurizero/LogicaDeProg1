def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


numero = int(input("Digite a posição do termo de Fibonacci que você quer: "))

print(f"O {numero}º termo da sequência de Fibonacci é {fibonacci(numero)}")
