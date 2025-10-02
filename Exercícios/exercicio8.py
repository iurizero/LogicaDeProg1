print("Calculadora de IMC")
print("------------------")
peso = float(input("\nDigite seu peso em kg: "))
altura = float(input("\nDigite sua altura em metros:"))

imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.2f}")
if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= imc < 24.9:
    print("Você está com o peso normal.")
elif 25 <= imc < 29.9:
    print("Você está com sobrepeso.")
elif 30 <= imc < 34.9:
    print("Você está com obesidade grau 1.")
elif 35 <= imc < 39.9:
    print("Você está com obesidade grau 2.")
else:
    print("Você está com obesidade grau 3.")