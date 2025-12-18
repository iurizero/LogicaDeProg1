contador = 1
total = 0
while contador <= 10:
    n1 = int(input(f"Digite o {contador} número: "))
    contador+=1
    total = total + n1
    
print(f"O valor da média dos 10 números foi de: {total/10}")