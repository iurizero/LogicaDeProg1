contador = 1
total = 0
n1 = 0

while contador <= 10:
    n1 = int(input(f"Digite o {contador} número, inteiro e positivo: "))
    while n1 < 0:
        n1 = int(input(f"O valor digitado para o {contador} número foi inválido, digite um valor INTEIRO e POSITIVO: "))
        
    total = total + n1
    contador += 1

print(f"A média dos 10 números positivos foi de: {total/10}")