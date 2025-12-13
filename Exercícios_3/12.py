texto = input("Digite uma string: ")

apenas_digitos = True

for i in texto:
    if i < '0' or i > '9':
        apenas_digitos = False
        break

if apenas_digitos:
    print("A string contém apenas dígitos.")
else:
    print("A string NÃO contém apenas dígitos.")
