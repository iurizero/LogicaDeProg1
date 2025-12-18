texto = str(input("Digite uma frase: "))
texto_final = ""

for i in texto:
    if not i.isdigit():
        texto_final += i
        
print(texto_final)