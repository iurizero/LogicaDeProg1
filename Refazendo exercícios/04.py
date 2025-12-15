frase = str(input("Digite uma frase:")).lower()

frase_final = frase.split()
contador = 0

for i in frase_final:
    print(f"A palavra {frase_final[contador]} aparece na posição {frase_final.index(i)+1}")
    contador+=1