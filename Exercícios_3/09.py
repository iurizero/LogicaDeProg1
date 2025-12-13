frase = str(input("Digite a frase desejada: "))

for i in range(11):
    print(f"Removendo caracteres indesejados: {i}0%")

frase_final = ""

for i in frase:
    if i.isalpha() or i.isspace():
        frase_final += i

print(f"\nA frase sem os caracteres indesejados é: {frase_final}")
    