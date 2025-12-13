texto = str(input("Digite o texto: "))
mascara = str(input("Informe a mascara pra alterar os caracteres: "))

texto_mascarado = ""

for i in texto:
    
    if i != " ":
        texto_mascarado += mascara
    elif i == " ":
        texto_mascarado += " "
         
print(f"O texto mascarado é: {texto_mascarado}")