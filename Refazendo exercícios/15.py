numero = str(input("Digite o valor: "))
tamanho = int(input("Digite o tamanho mínimo: "))
caractere= str(input("Digite o caractere de preenchimento: "))

while len(numero) < tamanho:
    numero = caractere + numero

print(numero)