nome = str(input("Digite o seu nome: "))
salario = float(input("Digite seu salário fixo: "))
vendas = float(input("Digite em R$ o valor de vendas do mês: "))

comissao = vendas*0.15

print(f"Olá {nome}! Seu salário fixo é de {salario}R$, seu salário final com comissão é de {salario+comissao}R$! Parabens!")