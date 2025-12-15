texto = str(input("Digite a palavra/frase: "))
descarte = str(input("Digite o caractere a ser removido: "))

texto_final = ""

for i in texto:
    if i != descarte:
        texto_final+=i
    
print(texto_final)