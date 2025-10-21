quilometragem = float(input("Digite a quantidade de KM's rodados com o veículo: "))
dias = int(input("Digite a quantidade de dias que passou com o veículo: "))

valor_final = (dias*60) + (quilometragem*0.15)

print(f"O valor total do seu aluguel foi de {valor_final} R$")