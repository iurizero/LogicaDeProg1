print("\nCalculadora de ano bissexto")
print("----------------------")
ano=int(input("\nDigite o ano selecionado: "))
while ano < 1 or ano > 9999:
    print("\nAno inválido! Tente novamente.")
    ano=int(input("\nDigite o ano selecionado: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"\nO ano {ano} é bissexto")
else:
    print(f"\nO ano {ano} não é bissexto")
print("----------------------")
print("Fim do programa")