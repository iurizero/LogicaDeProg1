texto = str(input("Digite uma frase: "))

texto2 = texto.split()
texto3 = []

for i in texto2:
    if i not in texto3:
        texto3.append(i)

texto_final =" ".join(texto3)
    
print(texto_final)