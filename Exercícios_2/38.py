n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = 0

if n1 > 10 or n1 < 0:
    print("Valor informado é inválido na primeira nota, encerrando programa")

elif n2 > 10 or n2 < 0:
    print("Valor informado é inválido na segunda nota, encerrando programa")

else:
    media = (n1+n2)/2
    print(media)