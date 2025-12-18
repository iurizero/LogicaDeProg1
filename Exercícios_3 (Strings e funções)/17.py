texto = input("Digite a frase bla bla: ")

palavra = ""
ja_escrita = []

for i in texto:
    if i != " ":
        palavra += i
    else:
        if palavra != "" and palavra not in ja_escrita:
            ja_escrita.append(palavra)
        palavra = ""

if palavra != "" and palavra not in ja_escrita:
    ja_escrita.append(palavra)

print(ja_escrita)
