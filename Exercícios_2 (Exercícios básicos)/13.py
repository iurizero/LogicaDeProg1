distancia = float(input("Informe a distância a ser percorrida em KM: "))
velocidade = float(input("Informe a velocidade média que irá percorrer o trajeto em KM/h: "))

vfinal = distancia/velocidade

horas = int(vfinal)
minutos = int((vfinal - horas) * 60)

print(f"O tempo final é de: {horas} hora(s) e {minutos} minuto(s).")