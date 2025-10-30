palavra = str(input("Digite uma palavra: "))

L1 = str(input("Digite a letra a ser substituida: "))
L2 = str(input("Digite a letra substituta: "))

nova_palavra = ''

for i in range(len(palavra)):
    if palavra[i] == L1:
        nova_palavra += L2
    else:
        nova_palavra += palavra[i]
        
print(nova_palavra)