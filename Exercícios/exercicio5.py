print("\nClassificação de Triângulos")
print("--------------------------\n")

a = float(input("Digite o valor do lado A: "))
b = float(input("Digite o valor do lado B: "))
c = float(input("Digite o valor do lado C: "))

while (a + b > c) and (a + c > b) and (b + c > a) == False:
    print("Os lados não formam um triângulo. Tente novamente.")
    a = float(input("Digite o valor do lado A: "))
    b = float(input("Digite o valor do lado B: "))
    c = float(input("Digite o valor do lado C: "))

if a == b and b == c:
    print("\nO triângulo é equilátero.")

elif a == b or a == c or b == c:
    print("\nO triângulo é isósceles.")

else:
    print("\nO triângulo é escaleno.")

print("--------------------------\n")