lista_notas = []
contador = 1
while contador <= 5:
    nota = float(input(f"Digite a nota {contador}: "))
    while nota < 0 or nota > 10:
        nota = float(input(f"O valor digitado foi inválido, redigite a nota {contador} entre 0 a 10: "))
    lista_notas.append(nota)
    print(lista_notas)
    contador += 1

resultado = sum(lista_notas) / len(lista_notas)

print(f"A média das notas é: {resultado:.2f}")

if resultado >= 7:
    print("\nAprovado por média")
elif resultado >= 3:
    print("\nAlino em recuperação")
else:
    print("Se fodeu")