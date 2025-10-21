mercadoria = float(input("Informe o valor da mercadoria em R$: "))
desconto = float(input("Informe o valor do desconto em %: "))

valor_final = mercadoria - (mercadoria * desconto/100)

print(f'O valor final com o desconto de {desconto}% é de {valor_final}R$')