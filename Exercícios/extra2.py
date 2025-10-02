print("\nSistema de pontuação em competição")
print("----------------------------------")

nota1 = float(input("Digite a primeira nota: "))
while nota1 < 0 or nota1 > 10:
    print("Nota inválida, insira valores de 0 a 10")
    nota1 = float(input("Digite a primeira nota: "))

nota2 = float(input("Digite a segunda nota: "))
while nota2 < 0 or nota2 > 10:
    print("Nota inválida, insira valores de 0 a 10")
    nota2 = float(input("Digite a segunda nota: "))

nota3 = float(input("Digite a terceira nota: "))
while nota3 < 0 or nota3 > 10:
    print("Nota inválida, insira valores de 0 a 10")
    nota3 = float(input("Digite a terceira nota: "))

# Remoção dos valores
notas = [nota1, nota2, nota3]
nota_meio = notas.copy()
nota_meio.remove(max(nota_meio))
nota_meio.remove(min(nota_meio))

menor_nota = min(notas)
maior_nota = max(notas)

# Sistema de pontos

pontos = 0

if nota1 >= 8.5 and nota2 >= 8.5 and nota3 >= 8.5:
    pontos += 2

if nota_meio[0] >= 9:
    pontos += 1.5

if menor_nota <= 5:
    pontos -= 1
    
if maior_nota - menor_nota < 3:
    pontos -= 0.5

print(f"Sua pontuação final foi de {pontos} pontos!")
    
