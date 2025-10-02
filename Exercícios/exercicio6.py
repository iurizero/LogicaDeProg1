print("Sistema de verificação de aprovados")
print("-------------------------------")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
faltas = int(input("Digite o número de faltas: "))

media = (nota1 + nota2) / 2
faltas_maximas = 5 # COMO O NUMERO DE AULA N FOI ESPECIFICADO DEIXEI 20 AULAS, ENTÃO 25% DE 20 = 5

if media >= 7 and faltas <= faltas_maximas:
    print("Aluno aprovado!")
elif media >=2 and faltas <= faltas_maximas:
    print("Aluno em recuperação.")
else:
    print("Aluno reprovado.")