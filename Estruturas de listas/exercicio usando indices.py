numeros = [0, 0, 0, 0, 0]
x = 0
while x < 5:
    x += 1
    numeros[x] = int(input(f"Número {x}:"))
    
while True:
    escolhido = int(input("Que posição você quer imprimir (0 para sair): "))
    if escolhido == 0:
        break
    print(f"Você escolheu o número: {numeros[escolhido-1]}")
