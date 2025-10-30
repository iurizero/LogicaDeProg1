import math

# Ler número inteiro
num = int(input("Digite um número inteiro: "))

# Verificar se é negativo
if num < 0:
    print("Número inválido")
else:
    # Calcular logaritmo natural (base e)
    logaritmo = math.log(num)
    print(f"Logaritmo natural de {num} ≈ {logaritmo:.4f}")
