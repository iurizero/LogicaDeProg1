binario = str(input("Digite um numero em binário: "))

contador = 0

for i in range (len(binario)):
    if binario[i] == "1":
        contador+=1
    
print(contador)