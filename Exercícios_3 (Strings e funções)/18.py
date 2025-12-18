frase = str(input("Digite a frase: "))

frase_nova = ""
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for i in frase:
    if i not in numeros:
        frase_nova += i
        
print(frase_nova)