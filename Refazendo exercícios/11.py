texto = input("Digite um texto (use Enter para quebrar linha):")

linha = ""

for caractere in texto:
    if caractere != "\n":
        linha += caractere
    else:
        print(linha)
        linha = ""
        
if linha != "":
    print(linha)