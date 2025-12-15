texto = str(input("Digite a palavra/frase: "))

texto_final = ""

for i in texto:
    if i.isalnum() or i.isspace():
        texto_final+=i

print(texto_final)