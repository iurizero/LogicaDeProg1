salario = float(input("Digite o salário inicial: "))
aumento = float(input("Digite o aumento em %: "))

salario_final = salario + (salario*aumento/100)

print(f'O salário final com o aumento é de: {salario_final:.2f}R$')