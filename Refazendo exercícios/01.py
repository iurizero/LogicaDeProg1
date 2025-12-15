frase = str(input("Digite uma frase: ")).lower()
palavra = str(input("Digite uma palavra pra checar: ")).lower()

frase_start = frase.startswith(palavra)

if frase_start:
    print(f"A frase começa com a palavra digitada: {palavra}")
else:
    print(f"A frase NÃO começa com a palavra digitada, ela começa com: {frase_start}")