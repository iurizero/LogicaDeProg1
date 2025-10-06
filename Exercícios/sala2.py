contador = 1
acumulador = []
valor = 0
print("Calculadora de media de 10 idades")

while contador <=10:
    valor = int(input("\nInforme o valor da idade da pessoa: "))
    acumulador.append(valor)
    contador += 1

media = sum(acumulador) / len(acumulador)
print(acumulador)

print(f"\nA média de idades é de: {media}")