def imprime_barra(tamanho, caractere):
    for i in range(tamanho):
        print(caractere, end='')
    print()
    
print("""Escolha uma opção para o tamanho da barra:
      1 - 10 caracteres
      2 - 20 caracteres
      3 - 30 caracteres""")

a = int(input("\nEscolha a opção de tamanho: "))

print("""Escolha uma opção para o caractere usado pra compor a barra:
      1 - "-"
      2 - "*"
      3 - "#" """)

b = int(input("\nEscolha a opção de caractere: "))

if a == 1:
    tamanho = 10
elif a == 2:
    tamanho = 20
elif a == 3:
    tamanho = 30
else:
    print("Opção de tamanho inválida")
    exit()

if b == 1:
    caractere = "-"
elif b == 2:
    caractere = "*"
elif b == 3:
    caractere = "#"
else:
    print("Opção de caractere inválida")
    exit()

imprime_barra(tamanho,caractere)
