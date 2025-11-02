notas = []


for i in range(15):
    a = float(input(f"Digite a {i+1} nota: "))
    notas.append(a)
    
medias = (sum(notas))/15

print(f"A média geral das 15 notas foi de {medias} pontos")