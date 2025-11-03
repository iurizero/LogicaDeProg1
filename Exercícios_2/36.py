n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
diferenca = 0

if n1 == n2:
    print("Os número são iguais e sua diferença é zero")

elif n1 > n2:
    diferenca = n1 - n2
    print("O primeiro número é maior")
    print(f"A diferença entre eles é de {diferenca}")

else:
    diferenca = n2 - n1
    print("O segundo número é maior")
    print(f"A diferença entre eles é de {diferenca}")