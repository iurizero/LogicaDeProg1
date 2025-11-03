sexo = str(input("Digite seu sexo, h para homens e f para mulheres: "))
altura_i = float(input("Digite sua altura em cm: "))
peso_ideal = 0
altura = altura_i/100

if sexo == "h" or sexo == "H":
    peso_ideal = (72.7*altura) - 58
    print(f"Seu peso ideal é de {peso_ideal:.2f}")
elif sexo == "f" or sexo == "F":
    peso_ideal = (62.1*altura) - 44.7
    print(f"Seu peso ideal é de {peso_ideal:.2f}")

else:
    print("Sexo informado é inválido, encerrando programa")
