print("\nCalculadora do Iuri")
print("-------------------")

print("\nEscolha a operação: (+ - * /)")
operacao = input("Operação: ")
while operacao not in ["+","-","*","/"]:
    print("Operação inválida. Tente novamente.")
    operacao = input("Operação: ")

num1 = float(input("\nDigite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
resultado = 0

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    while num2 == 0:
        print("Erro: Divisão por zero não é permitida.")
        num2 = int(input("Digite um segundo número diferente de zero: "))
    resultado = num1 / num2

print(f"\nO resultado de {num1} {operacao} {num2} é: {resultado}\n")