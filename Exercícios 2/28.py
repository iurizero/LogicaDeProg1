palavra = str(input("Digite uma palavra: "))
caractere = str(input("Digite um caractere pra substituir nas vogais: "))

vogais = "aeiouAEIOU"
numero_de_vogais = 0
nova_palavra = ""

for letra in palavra:
    if letra in vogais:
        numero_de_vogais += 1
        nova_palavra += caractere
    else:
        nova_palavra += letra
    
print(f"{nova_palavra}")
    
