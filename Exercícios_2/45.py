dia = int(input("Digite um dia da semana entre 1 e 7: "))

while dia > 7 or dia < 1:
    dia = int(input("Valor informado é inválido, digite um valor entre 1 e 7: "))
    
if dia == 1:
    print("Domingo!")
elif dia == 2:
    print("Segunda-feira!")
elif dia == 3:
    print("Terça-feira!")
elif dia == 4:
    print("Quarta-feira!")
elif dia == 5:
    print("Quinta-feira!")
elif dia == 6:
    print("Sexta-feira")
else:
    print("Sábado!")