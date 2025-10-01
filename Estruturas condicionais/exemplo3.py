tempo_de_uso=int(input("Insira quantos minutos você usou esse mês: "))
total=0
if tempo_de_uso<200:
    total=tempo_de_uso*0.20
elif tempo_de_uso>=200 and tempo_de_uso<400:
    total=tempo_de_uso*0.18
else:
    total=tempo_de_uso*0.15

print(f"Você vai pagar: R$ ", total)