n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))

media = ((n1*1) + (n2*1) + (n3*2))/4

if media >= 6:
    print("Aluno aprovado")
    print(media)
else:
    print("Aluno reprovado")
    print(media)
