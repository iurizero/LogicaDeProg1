salario = float(input("Digite o valor do seu salário líquido: "))
prestacao = float(input("Digite o valor de sua prestação: "))

if prestacao >= salario*0.2:
    print("Emprestimo negado")
    
else:
    print("Emprestimo concedido")