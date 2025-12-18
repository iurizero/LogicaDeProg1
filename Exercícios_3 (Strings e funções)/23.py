def area_quadrado(x, y):
    return x*y

base = float(input("Digite o tamano da base do quadrado em CM: "))
altura = float(input("Digite a altura do quadrado em CM: "))

resultado = area_quadrado(base,altura)

print(f"A área do quadrado é de: {resultado}")