numero = float(input("Digite um número negativo ou positivo: "))

if numero < 0:
    numero = max(numero, -numero)

print (numero)