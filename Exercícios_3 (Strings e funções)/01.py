frase = str(input("Digite a frase a ser verificada: "))
palavra = str(input("Digite a palavra pra checar se a frase inicia com ela: "))

slice = ""
for i in frase:
    if i != " ":
        slice += i 
    elif i == " ":
        break

print (slice)

slice2 = slice.lower()
palavra2 = palavra.lower() 

if slice2 == palavra2:
    print(f"A frase começa com a palavra '{palavra}', perfeito!")

else:
    print(f"Ops, a frase não começava com '{palavra}'' mas sim com '{slice}'")

