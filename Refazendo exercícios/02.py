frase1 = str(input("Digite uma frase: ")).lower()
frase2 = str(input("Digite outra frase: ")).lower()

if frase2 in frase1:
    posicao = frase1.find(frase2)
    print(f"A segunda frase aparece dentro da primeira na posição: {posicao+1}")
else:
    print("A segunda frase NÃO aparece na primeira")