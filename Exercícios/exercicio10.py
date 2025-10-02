print("\nCalculadora de descontos progressiva")
print("--------------------------------------")

valor=float(input("\nInforme o valor da compra a ser efetuado: "))

while valor<0 or valor>10000:
    print("\nValor inválido! Tente novamente.")
    valor=float(input("\nInforme o valor da compra a ser efetuado: "))

if valor<=100:
    desconto=0
elif valor>100 and valor<=200:
    desconto=10
elif valor>200 and valor<=500:
    desconto=15
elif valor>500:
    desconto=20
    
valor_desconto=(valor*desconto)/100
valor_final=valor-valor_desconto
print(f"\nO valor do desconto é de {desconto}%")
print(f"\nO valor final do produto é de R$ {valor_final:.2f}")
print("\n--------------------------------------")

