
print("\nSistema de Análise de empréstimo bancário")
print("------------------------------------------")

renda_mensal=float(input("Digite sua renda mensal: "))
idade=int(input("Digite sua idade: "))
score_credito=int(input("Digite seu score de crédito (0 a 1000): "))
valor_emprestimo=float(input("Digite o valor do empréstimo: "))
prazo_pagamento=int(input("Digite o prazo de pagamento em meses: (12, 24, 36, 48 ou 60): "))
meses_possiveis = [12,24,36,48,60]

#Checagem de das informações solicitadas (Um saco)

while renda_mensal < 0 or renda_mensal > 100000:
    print("Valor inserido é inválido")
    renda_mensal=float(input("Digite sua renda mensal: "))

while prazo_pagamento not in meses_possiveis:
    print("Prazo de pagamento inválido.")
    prazo_pagamento=int(input("Digite o prazo de pagamento em meses: (12, 24, 36, 48 ou 60): "))

while idade < 0 or idade > 120:
    print("Idade inserida é inválida")
    idade=int(input("Digite sua idade: "))

while score_credito < 0 or score_credito > 1000:
    print("Score inserido é inválido")
    score_credito=int(input("Digite seu score de crédito (0 a 1000): "))
    
parcela = valor_emprestimo/prazo_pagamento #Calculada depois dos whiles pra evitar confusao antes da verificação

#condicionais pra reprovação imediata

if score_credito < 300:
    print("Infelizmente seu score de crédito não se encaixa nos padrões do empréstimo")
    print("O programa será encerrado imediatamente.")
    exit()

elif idade < 18 or idade > 70:
    print("Infelizmente sua idade não se encaixa nos padrões do empréstimo")
    print("O programa será encerrado imediatamente.")
    exit()

elif parcela > renda_mensal*0.4:
    print("Infelizmente a parcela do empréstimo solicitado ficará muito alta pra renda informada")
    print("O programa será encerrado imediatamente.")
    exit()
    
#Sistema de pontos pra aprovação

pontos = 0

if score_credito >= 800:
    pontos +=1
if renda_mensal > parcela*3:
    pontos +=1
if idade >=25 and idade <= 55:
    pontos +=1
if valor_emprestimo <= renda_mensal*10:
    pontos +=1
    
#Resposta aos pontos

if pontos == 1:
    print("\nAnálise humana necessária, trate o seu caso diretamente com nosso suporte: 0800-0000")

elif pontos>1:
    print("\nSeu crédito foi aprovado, iremos enviar o valor solicitado a sua conta do banco!")

else:
    print("\nInfelizmente não poderemos disponibilizar seu crédito, tente novamente em outro momento :)")
