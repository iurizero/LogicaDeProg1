texto = input("Digite uma string: ")

imprimivel = True

for caractere in texto:
    if ord(caractere) < 32 or ord(caractere) == 127:
        imprimivel = False
        break

if imprimivel:
    print("A string pode ser impressa.")
else:
    print("A string NÃO pode ser impressa.")
