frase1 = str(input("Digite a primeira palavra: ")).lower()
frase2 = str(input("Digite a segunda palavra: ")).lower()

frase_final = " "

if frase1 >= frase2:
    for i in frase1:
        if i in frase2:
            frase_final += i
else:
    for i in frase2:
        if i in frase1:
            frase_final += i 

print(f"A palavra formada com os caracteres em comum foi {frase_final}")

