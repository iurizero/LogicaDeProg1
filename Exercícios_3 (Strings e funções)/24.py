def area_triangulo(a, b):
    return (a*b)/2

base = float(input("Digite o tamanho da base do triangulo em CM: "))
altura = float(input("Digite a altura do triangulo em CM: "))

print(f"A área total do triangulo é de: {area_triangulo(base,altura)} centímetros quadrados!")