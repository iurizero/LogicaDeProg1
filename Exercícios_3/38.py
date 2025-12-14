# Funções que fazem cálculos
def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def calcular(funcao, x, y):
    return funcao(x, y)

print("""Escolha a operação:
1 - Soma
2 - Subtração
3 - Multiplicação
""")

opcao = int(input("Opção: "))

x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))


if opcao == 1:
    resultado = calcular(soma, x, y)
elif opcao == 2:
    resultado = calcular(subtrai, x, y)
elif opcao == 3:
    resultado = calcular(multiplica, x, y)
else:
    print("Opção inválida")
    exit()


print("Resultado:", resultado)
