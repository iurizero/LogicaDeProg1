salario_hora = float(input("Informe quanto você recebe por hora: "))

horas_trabalhadas = int(input("Informe as horas trabalhadas: "))

salario_total = salario_hora * horas_trabalhadas

inss = salario_total*0.11
sindicato = salario_total*0.05
impostorenda = salario_total*0.08
salario_final = salario_total - inss - sindicato - impostorenda

print(f"Você recebeu {salario_total}R$ de salario bruto este mês")

print(f"Você pagou {inss}R$ de imposto ao INSS este mês")

print(f"Você pagou {sindicato}R$ de contribuição ao sindicato este mês")

print(f"Seu salário líquido com descontos do IR, INSS e Sindicato foi de {salario_final}R$")