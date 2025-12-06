frase1 = str(input("Digite a primeira frase: "))
frase2 = str(input("Digite a segunda frase: "))

frase_formatada1 = frase1.lower()
frase_formatada2 = frase2.lower()

if frase_formatada2 in frase_formatada1:
    print("A segunda frase aparece na primeira")
else:
    print("A segunda frase NÃO aparece na primeira")

