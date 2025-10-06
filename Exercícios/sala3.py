print("\nCalculadora de poupança mensal")
print("---------------------------")

aporte = float(input("\nDigite o aporte inicial do projeto: "))
while aporte <= 0 or aporte > 1000000:
    aporte = float(input("\nValor informado é inválido\nInforme um valor entre 1 e 1 milhão: "))

meses = int(input("Digite o numero de meses em que o dinheiro vai ficar aplicado: "))
while meses < 1 or meses > 120:
    meses = int(input("\nValor informado é inválido\nInforme um valor entre 1 e 120 meses: "))

juros = float(input("Informe a taxa de juros desejada (SEM %): "))
while juros < 0 or juros > 100:
    juros = int(input("\nValor informado é inválido\nInforme um valor entre 1 e 100: "))

jurosf = juros/100
a = 0

while meses > 0:
    aporte = aporte+(aporte*jurosf)
    a +=1
    meses -= 1
    print(f"O valor mensal foi de R${aporte:.2f} no mes {a}")
    
print(f"\n O valor final do seu investimento é de R${aporte:.2f}")
print("\n------------------------------------")