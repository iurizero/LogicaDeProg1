print("Que dia é hoje?")
print("----------------")

dia = int(input("Digite o dia: "))

while dia < 1 or dia > 7:
    print("Dia inválido! Tente novamente.")
    dia = int(input("Digite o dia: "))

if dia == 1:
    print("Hoje é segunda-feira.")
elif dia == 2: 
    print("Hoje é terça-feira.")
elif dia == 3:
    print("Hoje é quarta-feira.")
elif dia == 4:
    print("Hoje é quinta-feira.")
elif dia == 5:
    print("Hoje é sexta-feira.")
elif dia == 6:
    print("Hoje é sábado.")
else:
    print("Hoje é domingo.")