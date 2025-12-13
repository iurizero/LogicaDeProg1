frase = input("Digite uma frase: ")

palavra = ""

for i in frase:
    if i != " ":
        palavra += i
    else:
        print(palavra)
        palavra = ""

if palavra != "":
    print(palavra)
