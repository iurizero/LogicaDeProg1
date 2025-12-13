numero = input("Digite um número: ")
tamanho_minimo = int(input("Digite o tamanho mínimo: "))
caractere = input("Digite o caractere de preenchimento: ")

resultado = numero

while len(resultado) < tamanho_minimo:
    resultado = caractere + resultado

print("Número formatado:", resultado)
