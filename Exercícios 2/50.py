a = 1
total = 0
inserir = 0
while a <= 10:
    inserir = float(input(f"Digite o {a} valor a ser somado: "))
    total = total + inserir
    a += 1
print(f"A soma total dos valores inseridos é de: {total}")