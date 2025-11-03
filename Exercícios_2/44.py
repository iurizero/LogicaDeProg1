nota_lab = float(input("Digite a nota do trabalho no laboratorio: "))
nota_semestre = float(input("Digite a nota da aval semestral: "))
nota_final = float(input("Digite a nota do exame final: "))

while nota_lab < 0 or nota_lab > 10:
    nota_lab = float(input("Valor inválido pra nota do laboratório, informe um valor entre 0 e 10: "))
while nota_semestre < 0 or nota_semestre > 10:
    nota_semestre = float(input("Valor inválido pra nota do exame semestral, informe um valor entre 0 e 10: "))
while nota_final < 0 or nota_final > 10:
    nota_lab = float(input("Valor inválido pra nota do exame final, informe um valor entre 0 e 10: "))

media = ((nota_lab*2)+(nota_semestre*3)+(nota_final*5)) / 10

if media >= 0 and media <= 2.9:
    print("Reprovado direto")
    
elif media > 2.9 and media <= 4.9:
    print("Aluno em recuperação")

else:
    print("Aluno aprovado")