texto = str(input("Digite uma palavra pra ser formatada: "))
formatador = int(input("Digite um valor pra formatar todas as palavras de maneira igual: "))

texto_lista = texto.split()
texto_lista2 = []

for i in texto_lista:
    texto_lista2.append(i[:formatador:])

texto_final = " ".join(texto_lista2)

print(texto_final)