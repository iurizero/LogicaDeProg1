texto1 = str(input("Digite a primeira string: ")).lower()
texto2 = str(input("Digite a segunda string: ")).lower()

texto_final = ""

if len(texto1) > len(texto2):
    for i in texto1:
        if i not in texto2:
            texto_final+=i
else:
    for i in texto2:
        if i not in texto1:
            texto_final+=i

print(texto_final)